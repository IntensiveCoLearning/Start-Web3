import os
import subprocess
import re
import requests
from datetime import datetime, timedelta
import pytz
import logging

# Constants
START_DATE = datetime.fromisoformat(os.environ.get(
    'START_DATE', '2025-03-03T00:00:00+00:00')).replace(tzinfo=pytz.UTC)
END_DATE = datetime.fromisoformat(os.environ.get(
    'END_DATE', '2025-03-23T23:59:59+00:00')).replace(tzinfo=pytz.UTC)
DEFAULT_TIMEZONE = 'Asia/Shanghai'
FILE_SUFFIX = '.md'
README_FILE = 'README.md'
FIELD_NAME = 'Name'
Content_START_MARKER = "<!-- Content_START -->"
Content_END_MARKER = "<!-- Content_END -->"
TABLE_START_MARKER = "<!-- START_COMMIT_TABLE -->"
TABLE_END_MARKER = "<!-- END_COMMIT_TABLE -->"
GITHUB_REPOSITORY_OWNER = os.environ.get('GITHUB_REPOSITORY_OWNER')
GITHUB_REPOSITORY = os.environ.get('GITHUB_REPOSITORY')
STATS_START_MARKER = "<!-- STATISTICALDATA_START -->"
STATS_END_MARKER = "<!-- STATISTICALDATA_END -->"

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def print_env():
    print(f"""
            START_DATE: {START_DATE}
            END_DATE: {END_DATE}
            DEFAULT_TIMEZONE: {DEFAULT_TIMEZONE}
            FILE_SUFFIX: {FILE_SUFFIX}
            README_FILE: {README_FILE}
            FIELD_NAME: {FIELD_NAME}
            Content_START_MARKER: {Content_START_MARKER}
            Content_END_MARKER: {Content_END_MARKER}
            TABLE_START_MARKER: {TABLE_START_MARKER}
            TABLE_END_MARKER: {TABLE_END_MARKER}
            """)

def print_variables(*args, **kwargs):
    def format_value(value):
        if isinstance(value, str) and ('\n' in value or '\r' in value):
            return f'"""\n{value}\n"""'
        return repr(value)

    variables = {}
    for arg in args:
        if isinstance(arg, dict):
            variables.update(arg)
        else:
            variables[arg] = eval(arg)
    variables.update(kwargs)
    for name, value in variables.items():
        print(f"{name}: {format_value(value)}")

def get_date_range():
    return [START_DATE + timedelta(days=x) for x in range((END_DATE - START_DATE).days + 1)]

def get_user_timezone(file_content):
    yaml_match = re.search(r'---\s*\ntimezone:\s*(\S+)\s*\n---', file_content)
    if yaml_match:
        timezone_str = yaml_match.group(1)
        try:
            return pytz.timezone(timezone_str)
        except pytz.exceptions.UnknownTimeZoneError:
            try:
                offset = int(timezone_str[3:])
                return pytz.FixedOffset(offset * 60)
            except ValueError:
                logging.warning(f"Invalid timezone format: {timezone_str}. Using default {DEFAULT_TIMEZONE}.")
                return pytz.timezone(DEFAULT_TIMEZONE)
    return pytz.timezone(DEFAULT_TIMEZONE)

def extract_content_between_markers(file_content):
    start_index = file_content.find(Content_START_MARKER)
    end_index = file_content.find(Content_END_MARKER)
    if start_index == -1 or end_index == -1:
        logging.warning("Content_START_MARKER markers not found in the file")
        return ""
    return file_content[start_index + len(Content_START_MARKER):end_index].strip()

def find_date_in_content(content, local_date):
    date_patterns = [
        r'#\s*' + local_date.strftime("%Y.%m.%d"),
        r'##\s*' + local_date.strftime("%Y.%m.%d"),
        r'###\s*' + local_date.strftime("%Y.%m.%d"),
        r'#\s*' + local_date.strftime("%Y.%m.%d").replace('.0', '.'),
        r'##\s*' + local_date.strftime("%Y.%m.%d").replace('.0', '.'),
        r'###\s*' + local_date.strftime("%Y.%m.%d").replace('.0', '.'),
        r'#\s*' + local_date.strftime("%m.%d").lstrip('0').replace('.0', '.'),
        r'##\s*' + local_date.strftime("%m.%d").lstrip('0').replace('.0', '.'),
        r'###\s*' + local_date.strftime("%m.%d").lstrip('0').replace('.0', '.'),
        r'#\s*' + local_date.strftime("%Y/%m/%d"),
        r'##\s*' + local_date.strftime("%Y/%m/%d"),
        r'###\s*' + local_date.strftime("%Y/%m/%d"),
        r'#\s*' + local_date.strftime("%m/%d").lstrip('0').replace('/0', '/'),
        r'##\s*' + local_date.strftime("%m/%d").lstrip('0').replace('/0', '/'),
        r'###\s*' + local_date.strftime("%m/%d").lstrip('0').replace('/0', '/'),
        r'#\s*' + local_date.strftime("%m.%d").zfill(5),
        r'##\s*' + local_date.strftime("%m.%d").zfill(5),
        r'###\s*' + local_date.strftime("%m.%d").zfill(5)
    ]
    combined_pattern = '|'.join(date_patterns)
    return re.search(combined_pattern, content)

def get_content_for_date(content, start_pos):
    next_date_pattern = r'###\s*(\d{4}\.)?(\d{1,2}[\.\/]\d{1,2})'
    next_date_match = re.search(next_date_pattern, content[start_pos:])
    if next_date_match:
        return content[start_pos:start_pos + next_date_match.start()]
    return content[start_pos:]

def check_md_content(file_content, date, user_tz):
    try:
        content = extract_content_between_markers(file_content)
        local_date = date.astimezone(user_tz).replace(hour=0, minute=0, second=0, microsecond=0)
        current_date_match = find_date_in_content(content, local_date)

        if not current_date_match:
            logging.info(f"No match found for date {local_date.strftime('%Y-%m-%d')}")
            return False

        date_content = get_content_for_date(content, current_date_match.end())
        date_content = re.sub(r'\s', '', date_content)
        logging.info(f"Content length for {local_date.strftime('%Y-%m-%d')}: {len(date_content)}")
        return len(date_content) > 10
    except Exception as e:
        logging.error(f"Error in check_md_content: {str(e)}")
        return False

def get_user_study_status(nickname):
    user_status = {}
    file_name = f"{nickname}{FILE_SUFFIX}"
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            file_content = file.read()
        user_tz = get_user_timezone(file_content)
        logging.info(f"File content length for {nickname}: {len(file_content)} user_tz: {user_tz}")
        current_date = datetime.now(user_tz).replace(hour=0, minute=0, second=0, microsecond=0)

        for date in get_date_range():
            local_date = date.astimezone(user_tz).replace(hour=0, minute=0, second=0, microsecond=0)
            if date.day == current_date.day:
                user_status[date] = "✅" if check_md_content(file_content, date, pytz.UTC) else " "
            elif date > current_date:
                user_status[date] = " "
            else:
                user_status[date] = "✅" if check_md_content(file_content, date, pytz.UTC) else "⭕️"
        logging.info(f"Successfully processed file for user: {nickname}")
    except FileNotFoundError:
        logging.error(f"Error: Could not find file {file_name}")
        user_status = {date: "⭕️" for date in get_date_range()}
    except Exception as e:
        logging.error(f"Unexpected error processing file for {nickname}: {str(e)}")
        user_status = {date: "⭕️" for date in get_date_range()}
    return user_status

def check_weekly_status(user_status, date, user_tz):
    try:
        local_date = date.astimezone(user_tz).replace(hour=0, minute=0, second=0, microsecond=0)
        week_start = (local_date - timedelta(days=local_date.weekday()))
        week_dates = [week_start + timedelta(days=x) for x in range(7)]
        current_date = datetime.now(user_tz).replace(hour=0, minute=0, second=0, microsecond=0)
        week_dates = [d for d in week_dates if d.astimezone(pytz.UTC).date() in [
            date.date() for date in get_date_range()] and d <= min(local_date, current_date)]

        missing_days = sum(1 for d in week_dates if user_status.get(datetime.combine(
            d.astimezone(pytz.UTC).date(), datetime.min.time()).replace(tzinfo=pytz.UTC), "⭕️") == "⭕️")

        if local_date == current_date and missing_days > 2:
            return "❌"
        elif local_date < current_date and missing_days > 2:
            return "❌"
        elif local_date > current_date:
            return " "
        else:
            return user_status.get(datetime.combine(date.date(), datetime.min.time()).replace(tzinfo=pytz.UTC), "⭕️")
    except Exception as e:
        logging.error(f"Error in check_weekly_status: {str(e)}")
        return "⭕️"

def get_all_user_files():
    exclude_prefixes = ('template', 'readme')
    return [f[:-len(FILE_SUFFIX)] for f in os.listdir('.')
            if f.lower().endswith(FILE_SUFFIX.lower())
            and not f.lower().startswith(exclude_prefixes)]

def extract_name_from_row(row):
    match = re.match(r'\|\s*\[([^\]]+)\]\([^)]+\)\s*\|', row)
    if match:
        return match.group(1).strip()
    else:
        parts = row.split('|')
        if len(parts) > 1:
            return parts[1].strip()
        return None

def update_readme(content):
    try:
        start_index = content.find(TABLE_START_MARKER)
        end_index = content.find(TABLE_END_MARKER)
        if start_index == -1 or end_index == -1:
            logging.error("Error: Couldn't find the table markers in README.md")
            return content

        new_table = [
            f'{TABLE_START_MARKER}\n',
            f'| {FIELD_NAME} | ' + ' | '.join(date.strftime("%m.%d").lstrip('0')
                       for date in get_date_range()) + ' |\n',
            '| ------------- | ' + ' | '.join(['----' for _ in get_date_range()]) + ' |\n'
        ]

        existing_users = set()
        table_rows = content[start_index + len(TABLE_START_MARKER):end_index].strip().split('\n')[2:]

        for row in table_rows:
            user_name = extract_name_from_row(row)
            if user_name:
                existing_users.add(user_name)
                new_table.append(generate_user_row(user_name))
            else:
                logging.warning(f"Skipping invalid row: {row}")

        new_users = set(get_all_user_files()) - existing_users
        for user in new_users:
            if user.strip():
                new_table.append(generate_user_row(user))
                logging.info(f"Added new user: {user}")
            else:
                logging.warning(f"Skipping empty user: '{user}'")
        new_table.append(f'{TABLE_END_MARKER}\n')
        return content[:start_index] + ''.join(new_table) + content[end_index + len(TABLE_END_MARKER):]
    except Exception as e:
        logging.error(f"Error in update_readme: {str(e)}")
        return content

def generate_user_row(user):
    user_status = get_user_study_status(user)
    owner, repo = get_repo_info()
    if owner and repo:
        repo_url = f"https://github.com/{owner}/{repo}/blob/main/{user}{FILE_SUFFIX}"
    else:
        repo_url = f"{user}{FILE_SUFFIX}"
    user_link = f"[{user}]({repo_url})"
    new_row = f"| {user_link} |"
    is_eliminated = False
    absent_count = 0
    current_week = None

    file_name_to_open = f"{user}{FILE_SUFFIX}"
    try:
        with open(file_name_to_open, 'r', encoding='utf-8') as file:
            file_content = file.read()
    except FileNotFoundError:
        logging.error(f"Error: Could not find file {file_name_to_open}")
        return "| " + user_link + " | " + " ⭕️ |" * len(get_date_range()) + "\n"

    user_tz = get_user_timezone(file_content)
    user_current_day = datetime.now(user_tz).replace(hour=0, minute=0, second=0, microsecond=0)
    for date in get_date_range():
        user_datetime = date.astimezone(pytz.UTC).replace(hour=0, minute=0, second=0, microsecond=0)
        if is_eliminated or (user_datetime > user_current_day and user_datetime.day > user_current_day.day):
            new_row += " |"
        else:
            user_date = user_datetime
            week = user_date.isocalendar()[1]
            if week != current_week:
                current_week = week
                absent_count = 0
            status = user_status.get(user_date, "")
            if status == "⭕️":
                absent_count += 1
                if absent_count > 2:
                    is_eliminated = True
                    new_row += " ❌ |"
                else:
                    new_row += " ⭕️ |"
            else:
                new_row += f" {status} |"
    return new_row + '\n'

def get_repo_info():
    if 'GITHUB_REPOSITORY' in os.environ:
        full_repo = os.environ['GITHUB_REPOSITORY']
        owner, repo = full_repo.split('/')
    else:
        try:
            remote_url = subprocess.check_output(
                ['git', 'config', '--get', 'remote.origin.url']).decode('utf-8').strip()
            if remote_url.startswith('https://github.com/'):
                owner, repo = remote_url.split('/')[-2:]
            elif remote_url.startswith('git@github.com:'):
                owner, repo = remote_url.split(':')[-1].split('/')
            else:
                raise ValueError("Unsupported remote URL format")
            repo = re.sub(r'\.git$', '', repo)
        except subprocess.CalledProcessError:
            logging.error("Failed to get repository information from git config")
            return None, None
    return owner, repo

def get_fork_count():
    owner, repo = get_repo_info()
    if not owner or not repo:
        logging.error("Failed to get repository information")
        return None
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    try:
        response = requests.get(api_url, timeout=10.0)
        response.raise_for_status()
        repo_data = response.json()
        return repo_data['forks_count']
    except requests.RequestException as e:
        logging.error(f"Error fetching fork count: {e}")
        return None

def calculate_statistics(content):
    start_index = content.find(STATS_START_MARKER)
    end_index = content.find(STATS_END_MARKER)
    if start_index == -1 or end_index == -1:
        logging.error("Error: Couldn't find the stats markers in README.md")
        return None

    stats_content = content[start_index + len(STATS_START_MARKER):end_index].strip()
    stats = {
        "total_participants": 0,
        "eliminated_participants": 0,
        "completed_participants": 0,
        "perfect_attendance_users": [],
        "completed_users": [],
        "fork_count": 0
    }

    total_match = re.search(r"- 总参与人数:\s*(\d+)", stats_content)
    if total_match:
        stats["total_participants"] = int(total_match.group(1))

    completed_match = re.search(r"- 完成人数:\s*(\d+)", stats_content)
    if completed_match:
        stats["completed_participants"] = int(completed_match.group(1))

    completed_users_match = re.search(r"- 完成用户:\s*([\w\s,]+)", stats_content)
    if completed_users_match:
        stats["completed_users"] = [x.strip() for x in completed_users_match.group(1).split(',') if x.strip()]

    perfect_attendance_users_match = re.search(r"- 全勤用户:\s*([\w\s,]+)", stats_content)
    if perfect_attendance_users_match:
        stats["perfect_attendance_users"] = [
            x.strip() for x in perfect_attendance_users_match.group(1).split(',') if x.strip()]

    eliminated_match = re.search(r"- 淘汰人数:\s*(\d+)", stats_content)
    if eliminated_match:
        stats["eliminated_participants"] = int(eliminated_match.group(1))

    fork_count_match = re.search(r"- Fork人数:\s*(\d+)", stats_content)
    if fork_count_match:
        stats["fork_count"] = int(fork_count_match.group(1))

    return stats

def update_statistics(content, stats):
    start_index = content.find(STATS_START_MARKER)
    end_index = content.find(STATS_END_MARKER)
    if start_index == -1 or end_index == -1:
        logging.error("Error: Couldn't find the stats markers in README.md")
        return content

    stats_text = f"""{STATS_START_MARKER}
## 统计数据

- 总参与人数: {stats["total_participants"]}
- 完成人数: {stats["completed_participants"]}
- 完成用户: {', '.join(stats['completed_users'])}
- 全勤用户: {', '.join(stats['perfect_attendance_users'])}
- 淘汰人数: {stats["eliminated_participants"]}
- 淘汰率: {stats["total_participants"] and stats["eliminated_participants"] / stats["total_participants"]:.2%}
- Fork人数: {stats["fork_count"]}
{STATS_END_MARKER}"""
    return content[:start_index] + stats_text + content[end_index + len(STATS_END_MARKER):]

def update_statistics_after_end(content, user_files):
    """在活动结束后更新统计数据"""
    current_time = datetime.now(pytz.UTC)
    stats = {
        "total_participants": len(user_files),
        "eliminated_participants": 0,
        "completed_participants": 0,
        "perfect_attendance_users": [],
        "completed_users": [],
        "fork_count": get_fork_count() or 0
    }

    # 从表格中提取用户状态
    start_index = content.find(TABLE_START_MARKER)
    end_index = content.find(TABLE_END_MARKER)
    if start_index == -1 or end_index == -1:
        logging.error("Error: Couldn't find the table markers in README.md")
        return content

    table_content = content[start_index + len(TABLE_START_MARKER):end_index].strip()
    table_rows = table_content.split('\n')[2:]  # 跳过表头和分隔行
    
    for row in table_rows:
        user_name = extract_name_from_row(row)
        if not user_name:
            continue
            
        # 检查用户是否被淘汰（行中是否包含 ❌）
        is_eliminated = "❌" in row
        
        if is_eliminated:
            stats["eliminated_participants"] += 1
        else:
            # 如果用户没有被淘汰，则认为已完成
            stats["completed_users"].append(user_name)
            stats["completed_participants"] += 1
            
            # 检查是否全勤（行中只有 ✅ 或空格，没有 ⭕️）
            if "⭕️" not in row:
                check_marks = row.count("✅")
                if check_marks > 0:  # 至少有一个打卡记录
                    stats["perfect_attendance_users"].append(user_name)

    return update_statistics(content, stats)

def main():
    try:
        with open(README_FILE, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        logging.error(f"Error: Could not find file {README_FILE}")
        return

    current_time = datetime.now(pytz.UTC)
    user_files = get_all_user_files()

    # 无论如何先更新表格
    content = update_readme(content)

    # 如果当前时间超过结束日期，计算并更新统计数据
    if current_time > END_DATE:
        content = update_statistics_after_end(content, user_files)
        logging.info("Activity has ended. Final statistics have been calculated and updated.")
    else:
        # 在活动期间，仍然更新现有统计数据
        stats = calculate_statistics(content)
        if stats:
            content = update_statistics(content, stats)
        logging.info(f"Updated {README_FILE} - Activity still in progress")

    with open(README_FILE, 'w', encoding='utf-8') as file:
        file.write(content)

    logging.info(f"Successfully updated {README_FILE}")

if __name__ == "__main__":
    main()

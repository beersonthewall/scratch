def get_reports():
    with open('input.txt') as f:
        return f.readlines()

def check_report(report):
    prev = None
    for item in report:
        if not prev:
            prev = item
            continue

        diff = abs(item - prev)
        if diff < 1 or diff > 3:
            return False
        prev = item
        srt = list(sorted(report))
    if srt == report or srt == list(reversed(report)):
        return True
    return False

def report_to_list(report):
    report = report.strip()
    report = report.split(' ')
    report = list(map(lambda x: int(x), report))
    return report

def is_safe_report(report):
    return check_report(report_to_list(report))

def try_remove_level(report):
    report = report_to_list(report)
    for i in range(len(report)):
        report_clone = list(report)
        del report_clone[i]
        if check_report(report_clone):
            return True
    return False

def part_one():
    safe_reports = 0
    for report in get_reports():
        if is_safe_report(report):
            safe_reports += 1
    return safe_reports

def part_two():
    safe_reports = 0
    for report in get_reports():
        if is_safe_report(report):
            safe_reports += 1
        elif try_remove_level(report):
            safe_reports += 1

    return safe_reports

def main():
    print(part_one())
    print(part_two())

if __name__ == "__main__":
    main()

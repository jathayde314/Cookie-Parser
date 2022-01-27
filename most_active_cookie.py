import sys
import collections


class CookieParser:

    def __init__(self, argv=None):
        self.date = None
        self.cookieDict = collections.defaultdict(int)
        self.fileName = None
        if not argv:
            self.argv = sys.argv
        else:
            self.argv = argv

    def set_date_cli(self):
        for i in range(0, len(self.argv) - 1):
            if self.argv[i] == "-d":
                self.date = self.argv[i + 1]
                return
        raise ValueError("No Date Provided")

    def set_file(self, file):
        self.fileName = file
        return

    def set_file_cli(self):
        if len(self.argv) < 2:
            raise ValueError("No file provided")
        self.fileName = self.argv[1]

    def create_cookie_dict(self):
        if not self.fileName:
            raise ValueError("No file set")
        if not self.date:
            raise ValueError("No date set")
        file = open(self.fileName, 'r')

        # Reads labels from CSV
        line = file.readline()
        split_line = line.split(",")
        # Checks that CSV matches format
        if split_line[0] != "cookie" or split_line[1][:-1] != "timestamp":
            file.close()
            raise ValueError("CSV does not match format")
        
        # Gets first instance from CSV
        line = file.readline()
        
        while line:
            split_line = line.split(",")
            # Date is first 10 characters of UTC
            if split_line[1][0:10] == self.date:
                self.cookieDict[split_line[0]] += 1
            line = file.readline()
        file.close()
        return

    def find_max_cookie_activity(self):
        if not self.cookieDict.values():
            raise ValueError("No cookie activity on day")
        max_activity = max(self.cookieDict.values())
        return [key for key, val in self.cookieDict.items() if val == max_activity]

    def find_max_from_args(self):
        self.set_date_cli()
        self.set_file_cli()
        self.create_cookie_dict()
        return self.find_max_cookie_activity()


if __name__ == '__main__':
    parser = CookieParser(sys.argv)
    try:
        maxActCookies = parser.find_max_from_args()
    except ValueError as e:
        sys.exit(e)

    for cookie in maxActCookies:
        print(cookie)

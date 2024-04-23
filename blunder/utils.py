class FormatNumbers:
    @staticmethod
    def format_number(value):
        if value < 1000:
            return str(value)
        elif value < 1000000:
            return f"{value // 1000}k"
        elif value < 1000000000:
            return f"{value // 1000000}m"
        else:
            return f"{value // 1000000000}b"

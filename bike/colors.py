from os.path import abspath


class Color:
    styles_path = abspath("./bike/static/bike/styles.css")

    @staticmethod
    def get(color: str):
        if not hasattr(Color, 'colors'):
            print("Populating Colors")
            Color.colors = Color.get_colors()

        return Color.colors[color]

    @staticmethod
    def get_colors():
        with open(Color.styles_path, "r") as styles_file:
            lines = styles_file.readlines()

        colors = {}
        sub_scopes = 0
        state = 0
        for line in lines:
            match state:
                case 0:
                    if ":root" in line:
                        state = 1
                case 1:
                    if line.strip()[:2] == '/*':
                        continue

                    if "{" in line:
                        sub_scopes += 1
                    if "}" in line:
                        sub_scopes -= 1

                    parts = line.strip().replace(";", "").replace("--", "").split(':')
                    if len(parts) < 2:
                        if sub_scopes == -1:
                            break
                        continue
                    colors[parts[0].strip()] = parts[1].strip()
                    if sub_scopes == -1:
                        break
        return colors

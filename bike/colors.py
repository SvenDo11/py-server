from os.path import abspath


class Color:
    styles_path = abspath("./bike/static/bike/styles.css")

    @staticmethod
    def get(color: str):
        if not hasattr(Color, 'colors'):
            print("Populating Colors")
            Color.colors = Color.get_colors()

        return Color.colors[Color.get_key(color)]

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

    @staticmethod
    def get_key(name: str) -> str:
        name = name.lower()
        match name:
            case "color0" | "black":
                return "color0"
            case "color1" | "darkred":
                return "color1"
            case "color2" | "darkgreen":
                return "color2"
            case "color3" | "darkyellow":
                return "color3"
            case "color4" | "darkblue":
                return "color4"
            case "color5" | "darkmagenta":
                return "color5"
            case "color6" | "darkcyan":
                return "color6"
            case "color7" | "lightgrey":
                return "color7"
            case "color8" | "darkgrey":
                return "color8"
            case "color9" | "red":
                return "color9"
            case "color10" | "green":
                return "color10"
            case "color11" | "yellow":
                return "color11"
            case "color12" | "blue":
                return "color12"
            case "color13" | "magenta":
                return "color13"
            case "color14" | "cyan":
                return "color14"
            case "color15" | "white":
                return "color15"
            case _:
                return name

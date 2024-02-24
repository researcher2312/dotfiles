from libqtile.config import Group, Key
from libqtile.lazy import lazy


class CustomGroups:
    def __init__(self, names, labels):
        self.groups = []
        for i in range(0, len(names)):
            self.groups.append(Group(name=names[i], label=labels[i]))

    def extend_keys(self, CustomKeys):
        for i in self.groups:
            CustomKeys.keys.extend(
                [
                    # mod1 + letter of group = switch to group
                    Key(
                        [CustomKeys.mod],
                        i.name,
                        lazy.group[i.name].toscreen(),
                        desc="Switch to group {}".format(i.name),
                    ),
                    # mod1 + shift + letter of group = switch to & move focused window to group
                    Key(
                        [CustomKeys.mod, "shift"],
                        i.name,
                        lazy.window.togroup(i.name, switch_group=True),
                        desc="Switch to & move focused window to group {}".format(
                            i.name
                        ),
                    ),
                ]
            )

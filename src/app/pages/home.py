from os import environ

import dash
import dash_mantine_components as dmc
import requests
from dash import html
from dash_iconify import DashIconify

from app.lib.constants import PAGE_TITLE_PREFIX, PRIMARY_COLOR
from app.lib.directives.toc import TOC

dash.register_page(
    __name__,
    "/",
    title=PAGE_TITLE_PREFIX + "Home",
    description="Welcome to You There Solutions! Here you will find general information about the company as well as access to demos.",
)


def create_title(title, id):
    return dmc.Text(title, ta="center", fw=300, fz=30, id=id)


def create_heading(text):
    return dmc.Text(text, ta="center", mt=10, mb=20, mx=0)


# def create_contributors_avatars():
#     resp = requests.get(
#         "https://api.github.com/repos/snehilvj/dash-mantine-components/contributors",
#         headers={"authorization": f"token {environ['CONTRIB_TOKEN']}"},
#     )
#     contributors = resp.json()
#     children = []
#     for user in contributors:
#         avatar = dmc.Tooltip(
#             dmc.Anchor(dmc.Avatar(src=user["avatar_url"]), href=user["html_url"]),
#             label=user["login"],
#             position="bottom",
#         )
#         children.append(avatar)

#     return dmc.Group(children, justify="center")


def create_tile(icon, heading, description, href):
    return dmc.Card(
        radius="md",
        p="xl",
        withBorder=True,
        m=5,
        children=[
            DashIconify(
                icon=icon,
                height=20,
                color=dmc.DEFAULT_THEME["colors"][PRIMARY_COLOR][5],
            ),
            dmc.Anchor(
                href=href,
                children=dmc.Text(heading, size="lg", mt="md"),
            ),
            dmc.Text(description, size="sm", c="dimmed", mt="sm"),
        ],
    )


layout = html.Div(
    [
        dmc.Container(
            size="lg",
            mt=30,
            children=[
                create_title(
                    "You There Solutions",
                    id="features",
                ),
                dmc.Highlight(
                    "Look at our demos to find out how we can reduce you ongoing operational costs through the use of open source software and custom solutions. The solutions you want at the price point you need!",
                    ta="center",
                    mt=10,
                    mb=20,
                    mx=0,
                    highlight=["the solutions you want at the price point you need!"],
                ),
                # dmc.Group(
                #     [
                #         dmc.Anchor(dmc.Button("Get Started"), href="/getting-started"),
                #         dmc.Anchor(
                #             dmc.Button(
                #                 "Join Discord",
                #                 variant="outline",
                #                 leftSection=DashIconify(icon="bi:discord", width=20),
                #             ),
                #             href="https://discord.gg/KuJkh4Pyq5",
                #             target="_blank",
                #         ),
                #         dmc.Anchor(
                #             dmc.Button(
                #                 "Sponsor",
                #                 variant="outline",
                #                 color="red",
                #                 leftSection=DashIconify(
                #                     icon="akar-icons:heart", width=19
                #                 ),
                #             ),
                #             href="https://github.com/sponsors/snehilvj",
                #             target="_blank",
                #         ),
                #     ],
                #     justify="center",
                #     mt=30,
                #     mb=90,
                # ),
            ],
        ),
        dmc.Container(
            size="lg",
            px=0,
            py=0,
            my=40,
            children=[
                dmc.SimpleGrid(
                    mt=80,
                    cols={"xs": 1, "sm": 2, "xl": 3},
                    children=[
                        create_tile(
                            icon="akar-icons:calendar",
                            heading="24/7 Satellite Operations Automation",
                            description="Monitor and respond to anomalous sitauations across multiple command and control softwares without the need for defined APIs.",
                            href="/agc_monitor",
                        ),
                        # create_tile(
                        #     icon="uil:paint-tool",
                        #     heading="Dark Theme Support",
                        #     description="Use dark theme across all components with no additional steps.",
                        #     href="/components/mantineprovider",
                        # ),
                        # create_tile(
                        #     icon="ph:notification-bold",
                        #     heading="Notifications System",
                        #     description="Mantine has a great notifications system, and now you get that in dash apps "
                        #     "too.",
                        #     href="/components/notification",
                        # ),
                        # create_tile(
                        #     icon="radix-icons:dashboard",
                        #     heading="Responsive Grid System",
                        #     description="Design your layouts faster with DMC's Grid and SimpleGrid components.",
                        #     href="/components/grid",
                        # ),
                        # create_tile(
                        #     icon="el:gift",
                        #     heading="Unique Components",
                        #     description="Components such as Segmented Control only available with DMC.",
                        #     href="/components/segmentedcontrol",
                        # ),
                        # create_tile(
                        #     icon="lucide:text-cursor-input",
                        #     heading="Better Inputs",
                        #     description="Add label, description, errors, etc. easily to all inputs.",
                        #     href="/components/select",
                        # ),
                    ],
                )
            ],
        ),
        # dmc.Space(h=20),
        # create_title("Sponsors", id="sponsors"),
        # create_heading(
        #     dmc.Anchor(
        #         "Become a sponsor",
        #         underline=False,
        #         href="https://github.com/sponsors/snehilvj",
        #         target="_blank",
        #     )
        # ),
        # dmc.Group(
        #     [
        #         dcc.Link(
        #             dmc.Image(
        #                 src="https://avatars.githubusercontent.com/u/14855837?s=200&v=4",
        #                 alt="ascend.io",
        #                 h=85,
        #                 fit="contain",
        #             ),
        #             href="http://www.ascend.io",
        #             target="_blank",
        #         )
        #     ],
        #     justify="center",
        # ),
        # dmc.Space(h=40),
        # create_title("Contributors", id="contributors"),
        # create_heading(
        #     dmc.Anchor(
        #         "Become a contributor",
        #         underline=False,
        #         href="https://github.com/snehilvj/dash-mantine-components",
        #         target="_blank",
        #     )
        # ),
        # dmc.Space(h=10),
        # (create_contributors_avatars() if "CONTRIB_TOKEN" in environ else None),
        dmc.Space(h=40),
        dmc.Center(
            [
                dmc.Group(
                    gap="xs",
                    children=[
                        dmc.Text("Made with"),
                        DashIconify(icon="akar-icons:heart", width=19, color="red"),
                        dmc.Text("by Mihir Uppal"),
                    ],
                    justify="center",
                )
            ],
            h=100,
        ),
        # TOC.render(
        #     None,
        #     None,
        #     "Table of Contents",
        #     None,
        #     **{
        #         "table_of_contents": [
        #             (3, "Features", "features"),
        #             (3, "Sponsors", "sponsors"),
        #             (3, "Contributors", "contributors"),
        #         ]
        #     },
        # ),
    ]
)

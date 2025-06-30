from os import environ

import dash
import dash_mantine_components as dmc
import requests
from dash import html
from dash_iconify import DashIconify

from app.lib.constants import PAGE_TITLE_PREFIX, PRIMARY_COLOR
from app.lib.directives.toc import TOC
from app.lib.utils import get_unique_id

IDNS = get_unique_id(__file__)

dash.register_page(
    __name__,
    "/agc_monitor",
    title=PAGE_TITLE_PREFIX + "AGC Monitor",
    description="Demonstration of 24/7 satellite operations monitoring and response.",
    category="24/7 Satellite Operations"
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
            dmc.Text(heading, size="lg", mt="md"),
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
                    "AGC Monitoring and Response",
                    id="features",
                ),
                dmc.Highlight(
                    "This demo shows the ability to create a solutions which monitors two different unlike command and control softwares for an anomalous condition then respond accordingly.",
                    ta="center",
                    mt=10,
                    mb=20,
                    mx=0,
                    highlight=["two different"],
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
                    cols=2,
                    children=[
                        dmc.Stack(
                            children=[
                                dmc.Card(
                                    radius="md",
                                    p="xl",
                                    withBorder=True,
                                    m=5,
                                    children=[
                                        dmc.Text('Open MCT C2 System for SV 1', size="lg", mt="md"),
                                        dmc.Text('Command and control provided by open source Open MCT software.', size="sm", c="dimmed", mt="sm"),
                                        dmc.Anchor('C2 Instance', href='http://localhost:8080/')
                                    ],
                                ),
                                dmc.Card(
                                    radius="md",
                                    p="xl",
                                    withBorder=True,
                                    m=5,
                                    children=[
                                        dmc.Text('TLM Control', size="md", mt="md"),
                                        dmc.Switch(
                                            label='TLM Flow',
                                            id=IDNS+'tlm-flow-openmct-switch'
                                        ),
                                        dmc.Slider(label='AGC Control')
                                    ],
                                )
                            ]
                        ),
                        dmc.Stack(
                            children=[
                               dmc.Card(
                                    radius="md",
                                    p="xl",
                                    withBorder=True,
                                    m=5,
                                    children=[
                                        dmc.Text('Yamcs C2 System for SV 2', size="lg", mt="md"),
                                        dmc.Text('Command and control provided by open source Yamcs software.', size="sm", c="dimmed", mt="sm"),
                                    ],
                                ),
                                dmc.Card(
                                    radius="md",
                                    p="xl",
                                    withBorder=True,
                                    m=5,
                                    children=[
                                        dmc.Text('TLM Control', size="md", mt="md"),
                                        dmc.Switch(
                                            label='TLM Flow',
                                            id=IDNS+'tlm-flow-yamcs-switch'
                                        )
                                    ],
                                )
                            ]
                        )
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
        # dmc.Space(h=40),
        # dmc.Center(
        #     [
        #         dmc.Group(
        #             gap="xs",
        #             children=[
        #                 dmc.Text("Made with"),
        #                 DashIconify(icon="akar-icons:heart", width=19, color="red"),
        #                 dmc.Text("by Mihir Uppal"),
        #             ],
        #             justify="center",
        #         )
        #     ],
        #     h=100,
        # ),
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

# from dash import Dash, html, dcc
# import dash_mantine_components as dmc
# from dash_iconify import DashIconify
# import pandas as pd
# import plotly.express as px

# app = Dash(__name__)

# # Sample data for charts
# df = pd.DataFrame({
#     'x': range(10),
#     'y': [i**2 for i in range(10)]
# })

# # Create a sample line chart
# fig = px.line(df, x='x', y='y')

# def create_stat_card(title, value, icon, color):
#     return dmc.Card(
#         children=[
#             dmc.CardSection(
#                 dmc.Group(
#                     children=[
#                         dmc.Text(title, size="sm", color="dimmed"),
#                         DashIconify(icon=icon, width=20, color=color)
#                     ],
#                     position="apart"
#                 ),
#                 p="sm"
#             ),
#             dmc.CardSection(
#                 dmc.Text(value, size="xl", weight=700),
#                 p="sm"
#             )
#         ],
#         withBorder=True,
#         shadow="sm",
#         radius="md",
#         style={"height": "100%"}
#     )

# app.layout = dmc.Container(
#     children=[
#         dmc.Title("Dashboard Overview", order=1, align="center", mb="lg"),
        
#         # Main grid layout
#         dmc.Grid(
#             children=[
#                 # Left column
#                 dmc.Col(
#                     children=[
#                         # Stats cards row
#                         dmc.Grid(
#                             children=[
#                                 dmc.Col(
#                                     create_stat_card(
#                                         "Total Revenue",
#                                         "$54,321",
#                                         "carbon:currency-dollar",
#                                         "green"
#                                     ),
#                                     span=6
#                                 ),
#                                 dmc.Col(
#                                     create_stat_card(
#                                         "Active Users",
#                                         "1,234",
#                                         "carbon:user-avatar",
#                                         "blue"
#                                     ),
#                                     span=6
#                                 ),
#                             ],
#                             gutter="md",
#                             mb="md"
#                         ),
                        
#                         # Chart card
#                         dmc.Card(
#                             children=[
#                                 dmc.CardSection(
#                                     dmc.Text("Performance Metrics", weight=500),
#                                     withBorder=True,
#                                     p="sm"
#                                 ),
#                                 dmc.CardSection(
#                                     dcc.Graph(figure=fig),
#                                     p="sm"
#                                 )
#                             ],
#                             withBorder=True,
#                             shadow="sm",
#                             radius="md",
#                             mb="md"
#                         ),
#                     ],
#                     span=6
#                 ),
                
#                 # Right column
#                 dmc.Col(
#                     children=[
#                         # Activity feed card
#                         dmc.Card(
#                             children=[
#                                 dmc.CardSection(
#                                     dmc.Group(
#                                         [
#                                             dmc.Text("Recent Activity", weight=500),
#                                             dmc.Badge("New", color="red")
#                                         ],
#                                         position="apart"
#                                     ),
#                                     withBorder=True,
#                                     p="sm"
#                                 ),
#                                 dmc.Stack(
#                                     children=[
#                                         dmc.Alert(
#                                             "New user registration",
#                                             title="System Alert",
#                                             color="blue",
#                                             variant="light"
#                                         ),
#                                         dmc.Alert(
#                                             "Server load at 82%",
#                                             title="Performance",
#                                             color="yellow",
#                                             variant="light"
#                                         ),
#                                         dmc.Alert(
#                                             "Backup completed",
#                                             title="System Update",
#                                             color="green",
#                                             variant="light"
#                                         )
#                                     ],
#                                     p="md",
#                                     spacing="sm"
#                                 )
#                             ],
#                             withBorder=True,
#                             shadow="sm",
#                             radius="md",
#                             mb="md",
#                             style={"height": "calc(50% - 0.5rem)"}
#                         ),
                        
#                         # Settings card
#                         dmc.Card(
#                             children=[
#                                 dmc.CardSection(
#                                     dmc.Text("Quick Settings", weight=500),
#                                     withBorder=True,
#                                     p="sm"
#                                 ),
#                                 dmc.Stack(
#                                     children=[
#                                         dmc.Switch(
#                                             label="Notifications",
#                                             checked=True,
#                                             size="md"
#                                         ),
#                                         dmc.Switch(
#                                             label="Dark Mode",
#                                             checked=False,
#                                             size="md"
#                                         ),
#                                         dmc.Switch(
#                                             label="Auto Updates",
#                                             checked=True,
#                                             size="md"
#                                         )
#                                     ],
#                                     p="md",
#                                     spacing="md"
#                                 )
#                             ],
#                             withBorder=True,
#                             shadow="sm",
#                             radius="md",
#                             style={"height": "calc(50% - 0.5rem)"}
#                         )
#                     ],
#                     span=6
#                 )
#             ],
#             gutter="md"
#         )
#     ],
#     size="xl",
#     p="md",
#     style={"height": "100vh"}
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)
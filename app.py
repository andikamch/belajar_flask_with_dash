import dash
import dash_bootstrap_components as dbc
from dash import html
from flask import Flask

server = Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
)

user_name = "Andhika Machri Maulana"
NPM = "50424127"
kelas = "1IA11"
about = """Saya adalah seorang yang masih baru dalam bidang pemrograman, 
           saya memiliki rasa ingin tahu yang lumayan besar dan ingin mencoba berbagai macam bahasa yang tersedia untuk dipelajari, 
           saya memiliki hobi untuk berolahraga dan juga menulis, 
           selain itu saya juga suka sekali mendengarkan musik di saat saat senggang."""

app.layout = html.Div([
    html.Div([
        html.Div(style={
            'position': 'absolute',
            'top': 0,
            'left': 0,
            'right': 0,
            'bottom': 0,
            'backgroundColor': 'rgba(0, 0, 0, 0.6)',
            'zIndex': 1,
        }),
        dbc.Container([
            dbc.Row([
                dbc.Col(
                    html.Img(
                        src='static/profile.jpg',
                        className='img-fluid rounded-circle shadow',
                        style={
                            'width': '180px',
                            'height': '180px',
                            'objectFit': 'cover',
                            'marginBottom': '20px',
                            'border': '4px solid #fff',
                            'boxShadow': '0 4px 16px rgba(0,0,0,0.6)'
                        }
                    ),
                    xs=12, md=5,
                    className="d-flex justify-content-center justify-content-md-end align-items-center"
                ),
                dbc.Col(
                    html.Div([
                        html.P(
                            'Halo! Selamat Datang Di Portofolio Saya, Nama Saya',
                            className='lead text-white mb-2'
                        ),
                        html.H1(
                            user_name,
                            className='fw-bold text-white mb-2',
                            style={'fontSize': '2.5rem'}
                        ),
                        html.P(
                            f'Saya berasal dari kelas {kelas}',
                            className='text-white mb-2',
                            style={'fontSize': '1.3rem'}
                        ),
                        html.P(
                            f'NPM saya adalah {NPM}',
                            className='text-white mb-0',
                            style={'fontSize': '1.3rem'}
                        ),
                    ]),
                    xs=12, md=7, className="d-flex flex-column justify-content-center"
                )
            ],
            align="center",
            className="min-vh-100",
            style={'zIndex': 2}
            )
        ], fluid=True, style={
            'position': 'relative',
            'zIndex': 2,
            'height': '100vh'
        }),
    ], style={
        'backgroundImage': 'url("static/bg.jpg")',
        'backgroundSize': 'cover',
        'backgroundPosition': 'center',
        'position': 'relative',
        'minHeight': '100vh',
        'width': '100%',
        'overflow': 'hidden',
        'display': 'flex',
        'alignItems': 'center',
        'justifyContent': 'center',
    }),

    html.Div([
        dbc.Container(fluid=True, children=[
            html.H1(
                'About Me',
                style={
                    'textAlign': 'center',
                    'marginTop': '90px',
                    'paddingBottom': '0px',
                    'color': 'white'
                }
            ),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.Img(
                                        src='static/img3.jpg',
                                        style={
                                            'width': '100%',
                                            'height': 'auto',
                                            'marginTop': '28px',
                                            'borderRadius': '10px',
                                        },
                                        className="d-none d-md-block"
                                    ),
                                ], xs=12, md=6),

                                dbc.Col([
                                    html.Img(
                                        src='static/img2.png',
                                        style={
                                            'width': '100%',
                                            'height': 'auto',
                                            'borderRadius': '10px',
                                        },
                                        className="d-none d-md-block"
                                    ),
                                ], xs=12, md=6),
                            ])
                        ], style={'backgroundColor': '#4C585B'})
                    ],
                    className="d-none d-md-block",
                    style={
                        "width": "100%",
                        "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                        "marginTop": "50px",
                        'backgroundColor': '#393E46'
                    })
                ], xs=12, md=6),

                dbc.Col([
                    html.P(
                        about,
                        style={
                            'marginTop': '85px',
                            'fontWeight': 'bold',
                            'fontSize': '25px',
                            'textAlign': 'justify',
                            'color': 'white'
                        }
                    ),
                ], xs=12, md=6)
            ], align="center", justify="center")
        ])
    ], style={
        'backgroundColor': '#393E46',
        'padding': '40px 20px',
        'minHeight': '100vh',
        'fontFamily': 'sans-serif'
    }),
    html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col(
                        html.P(
                            'Made with ❤️ by Andhika © 2025. All rights reserved.',
                            className="text-white",
                        ),

                    xs=12, md=6, className="d-flex flex-column justify-content-center"
                ),
                dbc.Col(
                    html.Div([
                        html.P(
                            'Kontak saya:',
                            className='lead text-white mb-2',
                        ),
                        html.A(
                            'GitHub',
                            href='https://github.com/andikamch',
                            target='_blank',
                            className='lead text-white mb-2',
                        ),
                        html.P(
                            html.A(
                            'LinkedIn',
                            href='https://www.linkedin.com/in/andhika-machri-maulana-74ba0b32b/',
                            target='_blank',
                            className='lead text-white mb-2',
                        ),
                        )
                    ]),
                    xs=12, md=2, className="d-flex flex-column justify-content-end"
                )
            ]
            )
        ], fluid=True),
    
    ], style={
        'backgroundColor': '#000000',
        'padding': '40px 20px',
        'fontFamily': 'sans-serif'
    })
    
])



if __name__ == '__main__':
    server.run(debug=True)

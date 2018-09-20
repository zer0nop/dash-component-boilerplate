# pylint: disable=E1102

import dash_reactstrap
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

items = [
    {
        'src': 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22800%22%20height%3D%22400%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20800%20400%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_15ba800aa1d%20text%20%7B%20fill%3A%23555%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A40pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_15ba800aa1d%22%3E%3Crect%20width%3D%22800%22%20height%3D%22400%22%20fill%3D%22%23777%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22285.921875%22%20y%3D%22218.3%22%3EFirst%20slide%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E',
        'altText': 'Slide 1',
        'caption': 'Slide 1',
        'header': 'Slide 1 Header'
    },
    {
        'src': 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22800%22%20height%3D%22400%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20800%20400%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_15ba800aa20%20text%20%7B%20fill%3A%23444%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A40pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_15ba800aa20%22%3E%3Crect%20width%3D%22800%22%20height%3D%22400%22%20fill%3D%22%23666%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22247.3203125%22%20y%3D%22218.3%22%3ESecond%20slide%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E',
        'altText': 'Slide 2',
        'caption': 'Slide 2',
        'header': 'Slide 2 Header'
    },
    {
        'src': 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22800%22%20height%3D%22400%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20800%20400%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_15ba800aa21%20text%20%7B%20fill%3A%23333%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A40pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_15ba800aa21%22%3E%3Crect%20width%3D%22800%22%20height%3D%22400%22%20fill%3D%22%23555%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22277%22%20y%3D%22218.3%22%3EThird%20slide%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E',
        'altText': 'Slide 3',
        'caption': 'Slide 3',
        'header': 'Slide 3 Header'
    }
]

app.layout = html.Div([
    dash_reactstrap.Navbar(color='light', light=True, expand='md', children=[
        dash_reactstrap.NavbarBrand(tag="Nav", children=['Header']),
        dash_reactstrap.NavbarToggler(),
        dash_reactstrap.Collapse(navbar=True, children=[
            dash_reactstrap.Nav(className='ml-auto', navbar=True, children=[
                dash_reactstrap.NavItem(children=[
                    dash_reactstrap.NavLink(
                        href='/components/', children=['Components'])
                ]),
                dash_reactstrap.NavItem(children=[
                    dash_reactstrap.NavLink(
                        href='/components/', children=['Components'])
                ]),
                dash_reactstrap.UncontrolledDropdown(nav=True, inNavbar=True, children=[
                    dash_reactstrap.DropdownToggle(nav=True, caret=True, children=[
                        "Options"
                    ]),
                    dash_reactstrap.DropdownMenu(right=True, children=[
                        dash_reactstrap.DropdownItem(children=[
                            "Option 1"
                        ]),
                        dash_reactstrap.DropdownItem(children=[
                            "Option 2"
                        ]),
                        dash_reactstrap.DropdownItem(children=[
                            "Option 3"
                        ]),
                        dash_reactstrap.DropdownItem(children=[
                            "Option 4"
                        ]),
                    ])
                ]),
                dash_reactstrap.NavItem(children=[
                    dash_reactstrap.Form(inline=True, children=[
                        dash_reactstrap.FormGroup(className="mb-2 mr-sm-2 mb-sm-0", children=[
                            dash_reactstrap.Label(htmlFor="exampleEmail", className="mr-sm-2", children=[
                                "Email"
                            ]),
                            dash_reactstrap.Input(
                                type="email", name="email", id="exampleEmail", placeholder="something@idk.cool")
                        ]),
                        dash_reactstrap.FormGroup(className="mb-2 mr-sm-2 mb-sm-0", children=[
                            dash_reactstrap.Label(htmlFor="examplePassword", className="mr-sm-2", children=[
                                "Password"
                            ]),
                            dash_reactstrap.Input(
                                type="password", name="password", id="examplePassword", placeholder="don't tell!")
                        ]),
                        dash_reactstrap.Button(children=["Submit"])
                    ])
                ]),
            ])
        ]),
    ]),


    dash_reactstrap.Nav(tabs=True, children=[
        dash_reactstrap.NavItem(children=[
            dash_reactstrap.NavLink(
                        href='/components/', children=['Components'])
        ]),
        dash_reactstrap.NavItem(children=[
            dash_reactstrap.NavLink(active=True,
                                    href='/components/', children=['Components'])
        ]),
        dash_reactstrap.NavItem(children=[
            dash_reactstrap.NavLink(
                href='/components/', children=['Components'])
        ]),
        dash_reactstrap.NavItem(children=[
            dash_reactstrap.NavLink(
                href='/components/', children=['Components'])
        ]),
        dash_reactstrap.NavItem(children=[
            dash_reactstrap.NavLink(
                href='/components/', children=['Components'])
        ]),
    ]),

    html.Div(children=[
        dash_reactstrap.Button(color="primary", id="toggler", children=[
            "Toggle"
        ]),
        dash_reactstrap.UncontrolledCollapse(toggler="#toggler", children=[
            dash_reactstrap.Card(children=[
                dash_reactstrap.CardBody(children=[
                    '''
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt magni, voluptas debitis
                        similique porro a molestias consequuntur earum odio officiis natus, amet hic, iste sed
                        dignissimos esse fuga! Minus, alias.
                        '''
                ])
            ])
        ])
    ]),
    dash_reactstrap.UncontrolledCarousel(items=items),
    dash_reactstrap.ExampleComponent(
        id='input',
        value='my-value',
        label='my-label'
    ),
    dash_reactstrap.UncontrolledAlert(['Test']),
    # <div>
    #     <Navbar color="light" light expand="md">
    #       <NavbarBrand href="/">reactstrap</NavbarBrand>
    #       <NavbarToggler onClick={this.toggle} />
    #       <Collapse isOpen={this.state.isOpen} navbar>
    #         <Nav className="ml-auto" navbar>
    #           <NavItem>
    #             <NavLink href="/components/">Components</NavLink>
    #           </NavItem>
    #           <NavItem>
    #             <NavLink href="https://github.com/reactstrap/reactstrap">GitHub</NavLink>
    #           </NavItem>
    #           <UncontrolledDropdown nav inNavbar>
    #             <DropdownToggle nav caret>
    #               Options
    #             </DropdownToggle>
    #             <DropdownMenu right>
    #               <DropdownItem>
    #                 Option 1
    #               </DropdownItem>
    #               <DropdownItem>
    #                 Option 2
    #               </DropdownItem>
    #               <DropdownItem divider />
    #               <DropdownItem>
    #                 Reset
    #               </DropdownItem>
    #             </DropdownMenu>
    #           </UncontrolledDropdown>
    #         </Nav>
    #       </Collapse>
    #     </Navbar>
    #   </div>
    html.Div(id='output')
])


@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)

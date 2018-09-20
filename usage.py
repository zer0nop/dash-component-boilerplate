import dash_reactstrap
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash('')

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

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
                ])
            ])
        ])
    ]),
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

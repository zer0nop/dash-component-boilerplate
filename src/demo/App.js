/* eslint no-magic-numbers: 0 */
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as R from 'ramda';

import {
    ExampleComponent,
    Alert,
    Container,
    Row,
    Col,
    Navbar,
    NavbarBrand,
    NavbarToggler,
    Nav,
    NavItem,
    NavDropdown,
    NavLink,
    Breadcrumb,
    BreadcrumbItem,
    Button,
    ButtonDropdown,
    ButtonGroup,
    ButtonToolbar,
    Dropdown,
    DropdownItem,
    DropdownMenu,
    DropdownToggle,
    Fade,
    Badge,
    Card,
    CardLink,
    CardGroup,
    CardDeck,
    CardColumns,
    CardBody,
    CardBlock,
    CardFooter,
    CardHeader,
    CardImg,
    CardImgOverlay,
    Carousel,
    UncontrolledCarousel,
    CarouselControl,
    CarouselItem,
    CarouselIndicators,
    CarouselCaption,
    CardSubtitle,
    CardText,
    CardTitle,
    Popover,
    PopoverContent,
    PopoverBody,
    PopoverTitle,
    PopoverHeader,
    Progress,
    Modal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    PopperContent,
    Tooltip,
    Table,
    ListGroup,
    Form,
    FormFeedback,
    FormGroup,
    FormText,
    Input,
    InputGroup,
    InputGroupAddon,
    InputGroupButton,
    InputGroupButtonDropdown,
    InputGroupText,
    Label,
    CustomInput,
    Media,
    Pagination,
    PaginationItem,
    PaginationLink,
    TabContent,
    TabPane,
    Jumbotron,
    Collapse,
    ListGroupItem,
    ListGroupItemText,
    ListGroupItemHeading,
    UncontrolledAlert,
    UncontrolledButtonDropdown,
    UncontrolledCollapse,
    UncontrolledDropdown,
    UncontrolledNavDropdown,
    UncontrolledTooltip,
} from '../lib';


const items = [
    {
        src: 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22800%22%20height%3D%22400%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20800%20400%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_15ba800aa1d%20text%20%7B%20fill%3A%23555%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A40pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_15ba800aa1d%22%3E%3Crect%20width%3D%22800%22%20height%3D%22400%22%20fill%3D%22%23777%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22285.921875%22%20y%3D%22218.3%22%3EFirst%20slide%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E',
        altText: 'Slide 1',
        caption: 'Slide 1',
        header: 'Slide 1 Header'
    },
    {
        src: 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22800%22%20height%3D%22400%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20800%20400%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_15ba800aa20%20text%20%7B%20fill%3A%23444%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A40pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_15ba800aa20%22%3E%3Crect%20width%3D%22800%22%20height%3D%22400%22%20fill%3D%22%23666%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22247.3203125%22%20y%3D%22218.3%22%3ESecond%20slide%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E',
        altText: 'Slide 2',
        caption: 'Slide 2',
        header: 'Slide 2 Header'
    },
    {
        src: 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22800%22%20height%3D%22400%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20800%20400%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_15ba800aa21%20text%20%7B%20fill%3A%23333%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A40pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_15ba800aa21%22%3E%3Crect%20width%3D%22800%22%20height%3D%22400%22%20fill%3D%22%23555%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22277%22%20y%3D%22218.3%22%3EThird%20slide%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E',
        altText: 'Slide 3',
        caption: 'Slide 3',
        header: 'Slide 3 Header'
    }
];


console.log('App.js', Alert)

class App extends Component {

    constructor() {
        super();
        this.state = {
            value: ''
        }
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            <div>
                <ExampleComponent label='component-label'
                    setProps={this.setProps}
                    {...this.state}
                />
                <div>
                    <div>
                        <Nav tabs>
                            <NavItem>
                                <NavLink href="#" active>Link</NavLink>
                            </NavItem>
                            <Dropdown nav isOpen={this.state.dropdownOpen} toggle={this.toggle}>
                                <DropdownToggle nav caret>
                                    Dropdown
                                </DropdownToggle>
                                <DropdownMenu>
                                    <DropdownItem header>Header</DropdownItem>
                                    <DropdownItem disabled>Action</DropdownItem>
                                    <DropdownItem>Another Action</DropdownItem>
                                    <DropdownItem divider />
                                    <DropdownItem>Another Action</DropdownItem>
                                </DropdownMenu>
                            </Dropdown>
                            <NavItem>
                                <NavLink href="#">Link</NavLink>
                            </NavItem>
                            <NavItem>
                                <NavLink href="#">Another Link</NavLink>
                            </NavItem>
                            <NavItem>
                                <NavLink disabled href="#">Disabled Link</NavLink>
                            </NavItem>
                        </Nav>
                    </div>
                    <div>
                        <Button color="primary" id="toggler" style={{ marginBottom: '1rem' }}>
                            Toggle
                        </Button>
                        <UncontrolledCollapse toggler="#toggler">
                            <Card>
                                <CardBody>
                                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Nesciunt magni, voluptas debitis
                                    similique porro a molestias consequuntur earum odio officiis natus, amet hic, iste sed
                                    dignissimos esse fuga! Minus, alias.
                            </CardBody>
                            </Card>
                        </UncontrolledCollapse>
                    </div>
                    <UncontrolledCarousel items={items} />
                    <Navbar color="light" light expand="md">
                        <NavbarBrand href="/">reactstrap</NavbarBrand>
                        <NavbarToggler onClick={this.toggle} />
                        <Collapse isOpen={this.state.isOpen} navbar>
                            <Nav className="ml-auto" navbar>
                                <NavItem>
                                    <NavLink href="/components/">Components</NavLink>
                                </NavItem>
                                <NavItem>
                                    <NavLink href="https://github.com/reactstrap/reactstrap">GitHub</NavLink>
                                </NavItem>
                                <UncontrolledDropdown nav inNavbar>
                                    <DropdownToggle nav caret>
                                        Options
                                </DropdownToggle>
                                    <DropdownMenu right>
                                        <DropdownItem>
                                            Option 1
                                </DropdownItem>
                                        <DropdownItem>
                                            Option 2
                                </DropdownItem>
                                        <DropdownItem divider />
                                        <DropdownItem>
                                            Reset
                                </DropdownItem>
                                    </DropdownMenu>
                                </UncontrolledDropdown>
                            </Nav>
                        </Collapse>
                    </Navbar>
                </div>
                <div>
                    <Card>
                        <CardImg top width="100%" src="https://placeholdit.imgix.net/~text?txtsize=33&txt=318%C3%97180&w=318&h=180" alt="Card image cap" />
                        <CardBody>
                            <CardTitle>Card Title</CardTitle>
                            <CardText>This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</CardText>
                            <CardText>
                                <small className="text-muted">Last updated 3 mins ago</small>
                            </CardText>
                        </CardBody>
                    </Card>
                    <Card>
                        <CardBody>
                            <CardTitle>Card Title</CardTitle>
                            <CardText>This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</CardText>
                            <CardText>
                                <small className="text-muted">Last updated 3 mins ago</small>
                            </CardText>
                        </CardBody>
                        <CardImg bottom width="100%" src="https://placeholdit.imgix.net/~text?txtsize=33&txt=318%C3%97180&w=318&h=180" alt="Card image cap" />
                    </Card>
                </div>
                <div>
                    <Card>
                        <CardHeader>Header</CardHeader>
                        <CardBody>
                            <CardTitle>Special Title Treatment</CardTitle>
                            <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
                            <Button>Go somewhere</Button>
                        </CardBody>
                        <CardFooter>Footer</CardFooter>
                    </Card>

                    <Card>
                        <CardHeader tag="h3">Featured</CardHeader>
                        <CardBody>
                            <CardTitle>Special Title Treatment</CardTitle>
                            <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
                            <Button>Go somewhere</Button>
                        </CardBody>
                        <CardFooter className="text-muted">Footer</CardFooter>
                    </Card>
                </div>

                <div>
                    <Card body>
                        <CardTitle>Special Title Treatment</CardTitle>
                        <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
                        <Button>Go somewhere</Button>
                    </Card>
                    <Card body className="text-center">
                        <CardTitle>Special Title Treatment</CardTitle>
                        <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
                        <Button>Go somewhere</Button>
                    </Card>
                    <Card body className="text-right">
                        <CardTitle>Special Title Treatment</CardTitle>
                        <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
                        <Button>Go somewhere</Button>
                    </Card>
                </div>
                <Row>
                    <Col sm="6">
                        <Card body>
                            <CardTitle>Special Title Treatment</CardTitle>
                            <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
                            <Button>Go somewhere</Button>
                        </Card>
                    </Col>
                    <Col sm="6">
                        <Card body>
                            <CardTitle>Special Title Treatment</CardTitle>
                            <CardText>With supporting text below as a natural lead-in to additional content.</CardText>
                            <Button>Go somewhere</Button>
                        </Card>
                    </Col>
                </Row>
                <div style={{ width: '300px' }}>
                    <Card>
                        <CardBody>
                            <CardTitle>Card title</CardTitle>
                            <CardSubtitle>Card subtitle</CardSubtitle>
                        </CardBody>
                        <img width="100%" src="https://placeholdit.imgix.net/~text?txtsize=33&txt=318%C3%97180&w=318&h=180" alt="Card image cap" />
                        <CardBody>
                            <CardText>Some quick example text to build on the card title and make up the bulk of the card's content.</CardText>
                            <CardLink href="#">Card Link</CardLink>
                            <CardLink href="#">Another Link</CardLink>
                        </CardBody>
                    </Card>
                </div>
                <div style={{ width: '300px' }}>
                    <Card>
                        <CardImg top width="100%" src="https://placeholdit.imgix.net/~text?txtsize=33&txt=318%C3%97180&w=318&h=180" alt="Card image cap" />
                        <CardBody>
                            <CardTitle>Card title</CardTitle>
                            <CardSubtitle>Card subtitle</CardSubtitle>
                            <CardText>Some quick example text to build on the card title and make up the bulk of the card's content.</CardText>
                            <Button>Button</Button>
                        </CardBody>
                    </Card>
                </div>

                <ButtonGroup vertical>
                    <Button>1</Button>
                    <Button>2</Button>
                    <ButtonDropdown isOpen={this.state.dropdownOpen} toggle={this.toggle}>
                        <DropdownToggle caret>
                            Dropdown
                        </DropdownToggle>
                        <DropdownMenu>
                            <DropdownItem>Dropdown Link</DropdownItem>
                            <DropdownItem>Dropdown Link</DropdownItem>
                        </DropdownMenu>
                    </ButtonDropdown>
                </ButtonGroup>
                <br />
                <ButtonGroup>
                    <Button>1</Button>
                    <Button>2</Button>
                    <ButtonDropdown isOpen={this.state.dropdownOpen} toggle={this.toggle}>
                        <DropdownToggle caret>
                            Dropdown
                    </DropdownToggle>
                        <DropdownMenu>
                            <DropdownItem>Dropdown Link</DropdownItem>
                            <DropdownItem>Dropdown Link</DropdownItem>
                        </DropdownMenu>
                    </ButtonDropdown>
                </ButtonGroup>
                <br />
                <ButtonGroup size="lg">
                    <Button>Left</Button>
                    <Button>Middle</Button>
                    <Button>Right</Button>
                </ButtonGroup>
                <br />
                <ButtonGroup>
                    <Button>Left</Button>
                    <Button>Middle</Button>
                    <Button>Right</Button>
                </ButtonGroup>
                <br />
                <ButtonGroup size="sm">
                    <Button>Left</Button>
                    <Button>Middle</Button>
                    <Button>Right</Button>
                </ButtonGroup>
                <br />
                <ButtonToolbar>
                    <ButtonGroup>
                        <Button>1</Button>
                        <Button>2</Button>
                        <Button>3</Button>
                        <Button>4</Button>
                    </ButtonGroup>
                    <ButtonGroup>
                        <Button>5</Button>
                        <Button>6</Button>
                        <Button>7</Button>
                    </ButtonGroup>
                    <ButtonGroup>
                        <Button>8</Button>
                    </ButtonGroup>
                </ButtonToolbar>
                <br />
                <ButtonGroup>
                    <Button>Left</Button>
                    <Button>Middle</Button>
                    <Button>Right</Button>
                </ButtonGroup>

                <ButtonDropdown direction="right">
                    <DropdownToggle caret>
                        Dropright
                    </DropdownToggle>
                    <DropdownMenu>
                        <DropdownItem>Another Action</DropdownItem>
                        <DropdownItem>Another Action</DropdownItem>
                    </DropdownMenu>
                </ButtonDropdown>
                <ButtonDropdown direction="up">
                    <DropdownToggle caret>
                        Dropup
                    </DropdownToggle>
                    <DropdownMenu>
                        <DropdownItem>Another Action</DropdownItem>
                        <DropdownItem>Another Action</DropdownItem>
                    </DropdownMenu>
                </ButtonDropdown>
                <ButtonDropdown direction="left">
                    <DropdownToggle caret>
                        Dropleft
                    </DropdownToggle>
                    <DropdownMenu>
                        <DropdownItem>Another Action</DropdownItem>
                        <DropdownItem>Another Action</DropdownItem>
                    </DropdownMenu>
                </ButtonDropdown>
                <br />
                <ButtonDropdown>
                    <DropdownToggle caret size="lg">
                        Large Button
                    </DropdownToggle>
                    <DropdownMenu>
                        <DropdownItem>Another Action</DropdownItem>
                        <DropdownItem>Another Action</DropdownItem>
                    </DropdownMenu>
                </ButtonDropdown>

                <ButtonDropdown>
                    <DropdownToggle caret size="sm">
                        Small Button
                    </DropdownToggle>
                    <DropdownMenu>
                        <DropdownItem>Another Action</DropdownItem>
                        <DropdownItem>Another Action</DropdownItem>
                    </DropdownMenu>
                </ButtonDropdown>
                <ButtonDropdown>
                    <Button id="caret" color="primary">Split Button</Button>
                    <DropdownToggle caret color="primary" />
                    <DropdownMenu>
                        <DropdownItem header>Header</DropdownItem>
                        <DropdownItem disabled>Action</DropdownItem>
                        <DropdownItem>Another Action</DropdownItem>
                        <DropdownItem divider />
                        <DropdownItem>Another Action</DropdownItem>
                    </DropdownMenu>
                </ButtonDropdown>
                <ButtonDropdown>
                    <DropdownToggle caret color="primary">
                        Text
                    </DropdownToggle>
                    <DropdownMenu>
                        <DropdownItem header>Header</DropdownItem>
                        <DropdownItem disabled>Action</DropdownItem>
                        <DropdownItem>Another Action</DropdownItem>
                        <DropdownItem divider />
                        <DropdownItem>Another Action</DropdownItem>
                    </DropdownMenu>
                </ButtonDropdown>
                <ButtonDropdown>
                    <DropdownToggle caret>
                        Button Dropdown
                    </DropdownToggle>
                    <DropdownMenu>
                        <DropdownItem header>Header</DropdownItem>
                        <DropdownItem disabled>Action</DropdownItem>
                        <DropdownItem>Another Action</DropdownItem>
                        <DropdownItem divider />
                        <DropdownItem>Another Action</DropdownItem>
                    </DropdownMenu>
                </ButtonDropdown>
                <Button color="primary" size="lg" disabled>Primary button</Button>{' '}
                <Button color="secondary" size="lg" disabled>Button</Button>
                <Button color="primary" size="lg" active>Primary link</Button>{' '}
                <Button color="secondary" size="lg" active>Link</Button>
                <Button color="primary" size="lg" block>Block level button</Button>
                <Button color="secondary" size="lg" block>Block level button</Button>
                <Button color="primary" size="sm">Small Button</Button>{' '}
                <Button color="secondary" size="sm">Small Button</Button>
                <Button color="primary" size="lg">Large Button</Button>{' '}
                <Button color="secondary" size="lg">Large Button</Button>
                <div>
                    <Button outline color="primary">primary</Button>{' '}
                    <Button outline color="secondary">secondary</Button>{' '}
                    <Button outline color="success">success</Button>{' '}
                    <Button outline color="info">info</Button>{' '}
                    <Button outline color="warning">warning</Button>{' '}
                    <Button outline color="danger">danger</Button>
                </div>
                <div>
                    <Button color="primary">primary</Button>{' '}
                    <Button color="secondary">secondary</Button>{' '}
                    <Button color="success">success</Button>{' '}
                    <Button color="info">info</Button>{' '}
                    <Button color="warning">warning</Button>{' '}
                    <Button color="danger">danger</Button>{' '}
                    <Button color="link">link</Button>
                </div>
                <div>
                    <Breadcrumb tag="nav">
                        <BreadcrumbItem tag="a" href="#">Home</BreadcrumbItem>
                        <BreadcrumbItem tag="a" href="#">Library</BreadcrumbItem>
                        <BreadcrumbItem tag="a" href="#">Data</BreadcrumbItem>
                        <BreadcrumbItem active tag="span">Bootstrap</BreadcrumbItem>
                    </Breadcrumb>
                </div>
                <div>
                    <Breadcrumb>
                        <BreadcrumbItem active>Home</BreadcrumbItem>
                    </Breadcrumb>
                    <Breadcrumb>
                        <BreadcrumbItem><a href="#">Home</a></BreadcrumbItem>
                        <BreadcrumbItem active>Library</BreadcrumbItem>
                    </Breadcrumb>
                    <Breadcrumb>
                        <BreadcrumbItem><a href="#">Home</a></BreadcrumbItem>
                        <BreadcrumbItem><a href="#">Library</a></BreadcrumbItem>
                        <BreadcrumbItem active>Data</BreadcrumbItem>
                    </Breadcrumb>
                </div>
                <div>
                    <h1>Heading <Badge color="secondary">New</Badge></h1>
                    <h2>Heading <Badge color="secondary">New</Badge></h2>
                    <h3>Heading <Badge color="secondary">New</Badge></h3>
                    <h4>Heading <Badge color="secondary">New</Badge></h4>
                    <h5>Heading <Badge color="secondary">New</Badge></h5>
                    <h6>Heading <Badge color="secondary">New</Badge></h6>
                </div>
                <div>
                    <Button color="primary" outline>
                        Notifications <Badge color="secondary">4</Badge>
                    </Button>
                </div>
                <div>
                    <Badge color="primary">Primary</Badge>
                    <Badge color="secondary">Secondary</Badge>
                    <Badge color="success">Success</Badge>
                    <Badge color="danger">Danger</Badge>
                    <Badge color="warning">Warning</Badge>
                    <Badge color="info">Info</Badge>
                    <Badge color="light">Light</Badge>
                    <Badge color="dark">Dark</Badge>
                </div>
                <div>
                    <Badge color="primary" pill>Primary</Badge>
                    <Badge color="secondary" pill>Secondary</Badge>
                    <Badge color="success" pill>Success</Badge>
                    <Badge color="danger" pill>Danger</Badge>
                    <Badge color="warning" pill>Warning</Badge>
                    <Badge color="info" pill>Info</Badge>
                    <Badge color="light" pill>Light</Badge>
                    <Badge color="dark" pill>Dark</Badge>
                </div>
                <div>
                    <Badge href="#" color="primary">Primary</Badge>
                    <Badge href="#" color="secondary">Secondary</Badge>
                    <Badge href="#" color="success">Success</Badge>
                    <Badge href="#" color="danger">Danger</Badge>
                    <Badge href="#" color="warning">Warning</Badge>
                    <Badge href="#" color="info">Info</Badge>
                    <Badge href="#" color="light">Light</Badge>
                    <Badge href="#" color="dark">Dark</Badge>
                </div>
                <div>
                    <Alert color="success">
                        <h4 className="alert-heading">Well done!</h4>
                        <p>
                            Aww yeah, you successfully read this important alert message. This example text is going
                            to run a bit longer so that you can see how spacing within an alert works with this kind
                            of content.
                        </p>
                        <hr />
                        <p className="mb-0">
                            Whenever you need to, be sure to use margin utilities to keep things nice and tidy.
                        </p>
                    </Alert>
                </div>
                <div>
                    <Alert color="primary">
                        This is a primary alert with <a href="#" className="alert-link">an example link</a>. Give it a click if you like.
                    </Alert>
                    <Alert color="secondary">
                        This is a secondary alert with <a href="#" className="alert-link">an example link</a>. Give it a click if you like.
                    </Alert>
                    <Alert color="success">
                        This is a success alert with <a href="#" className="alert-link">an example link</a>. Give it a click if you like.
                    </Alert>
                    <Alert color="danger">
                        This is a danger alert with <a href="#" className="alert-link">an example link</a>. Give it a click if you like.
                    </Alert>
                    <Alert color="warning">
                        This is a warning alert with <a href="#" className="alert-link">an example link</a>. Give it a click if you like.
                    </Alert>
                    <Alert color="info">
                        This is a info alert with <a href="#" className="alert-link">an example link</a>. Give it a click if you like.
                    </Alert>
                    <Alert color="light">
                        This is a light alert with <a href="#" className="alert-link">an example link</a>. Give it a click if you like.
                    </Alert>
                    <Alert color="dark">
                        This is a dark alert with <a href="#" className="alert-link">an example link</a>. Give it a click if you like.
                    </Alert>
                </div>
                <div>
                    <Alert color="primary">
                        This is a primary alert — check it out!
                    </Alert>
                    <Alert color="secondary">
                        This is a secondary alert — check it out!
                    </Alert>
                    <Alert color="success">
                        This is a success alert — check it out!
                    </Alert>
                    <Alert color="danger">
                        This is a danger alert — check it out!
                    </Alert>
                    <Alert color="warning">
                        This is a warning alert — check it out!
                    </Alert>
                    <Alert color="info">
                        This is a info alert — check it out!
                    </Alert>
                    <Alert color="light">
                        This is a light alert — check it out!
                    </Alert>
                    <Alert color="dark">
                        This is a dark alert — check it out!
                    </Alert>
                </div>
            </div>
        )
    }
}

export default App;

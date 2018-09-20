import React from 'react';

export const DropDownContext = React.createContext({});

// This function takes a component...
export function withDropDownContext(Component) {
    // ...and returns another component...
    return function DropDownContextComponent(props) {
        // ... and renders the wrapped component with the context theme!
        // Notice that we pass through any additional props as well
        return (
            <DropDownContext.Consumer>
                {cntxt => <Component {...props} context={cntxt} />}
            </DropDownContext.Consumer>
        );
    };
}
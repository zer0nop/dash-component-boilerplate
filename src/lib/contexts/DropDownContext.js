import React from 'react';

export const DropDownContext = React.createContext({});

export function withDropDownContext(Component) {
    return function DropDownContextComponent(props) {
        return (
            <DropDownContext.Consumer>
                {cntxt => <Component {...props} context={cntxt} />}
            </DropDownContext.Consumer>
        );
    };
}
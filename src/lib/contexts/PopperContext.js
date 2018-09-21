import React from 'react';

export const PopperContext = React.createContext({});

export function withPopperContext(Component) {
    return function PopperContextComponent(props) {
        return (
            <PopperContext.Consumer>
                {cntxt => <Component {...props} context={cntxt} />}
            </PopperContext.Consumer>
        );
    };
}
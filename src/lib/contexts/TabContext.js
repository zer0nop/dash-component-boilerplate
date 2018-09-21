import React from 'react';

export const TabContext = React.createContext({});

export function withTabContext(Component) {
    return function TabContextComponent(props) {
        return (
            <TabContext.Consumer>
                {cntxt => <Component {...props} context={cntxt} />}
            </TabContext.Consumer>
        );
    };
}
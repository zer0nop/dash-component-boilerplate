import React from 'react';

export const CarouselContext = React.createContext({});

export function withCarouselContext(Component) {
    return function CarouselContextComponent(props) {
        return (
            <CarouselContext.Consumer>
                {cntxt => <Component {...props} context={cntxt} />}
            </CarouselContext.Consumer>
        );
    };
}
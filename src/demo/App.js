/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';

import { Import } from '../lib';

class App extends Component {

    constructor() {
        super();
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    render() {
        return (
            <h1>Import Demo</h1>
            <p>Nothing to see here as this component doesn't render anything.<br>
            But checkout your console, it should show output of 
            <a href='https://codepen.io/akronix/pen/pVqzLZ.js'>this codepen script</a> being imported</p>
            <div>
                <Import src='https://codepen.io/akronix/pen/pVqzLZ.js'/>
            </div>
        )
    }
}

export default App;

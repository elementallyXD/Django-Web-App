import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';

import Header from './layout/Header';
import DashBoard from './todos/DashBoard';

import { Provider } from 'react-redux';
import store from '../store';

class App extends Component {
    render() {
            return (
                <Provider store={store}>
                    //<Fragment>
                       <div className='container'>
                            <Header />
                            <DashBoard />
                       </div>
                    //</Fragment>
                </Provider>
            )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));
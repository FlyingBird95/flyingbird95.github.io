import React, {Component} from 'react';
import ReactGA from 'react-ga';
import $ from 'jquery';
import './App.css';
import Header from './Components/Header';
import Footer from './Components/Footer';
import About from './Components/About';
import Resume from './Components/Resume';
import Contact from './Components/Contact';
import Testimonials from './Components/Testimonials';
import Portfolio from './Components/Portfolio';

class App extends Component {

    constructor(props) {
        super(props);
        this.state = {
            data: {}
        };

        ReactGA.initialize('UA-110570651-1');
        ReactGA.pageview(window.location.pathname);
    }

    getData() {
        const load = document.getElementById('siteLoading')
        $.ajax({
            url: window.location.pathname + 'data.json',
            dataType: 'json',
            cache: false,
            success: function (data) {
                this.setState({data: data});
                setTimeout(() => {
                    load.outerHTML = '';
                }, 500)
            }.bind(this),
            error: function (xhr, status, err) {
                console.log(err);
            }
        });
    }

    componentDidMount() {
        this.getData();
    }


    render() {
        return (
            <div className="App">
                <Header data={this.state.data.main}/>
                <About data={this.state.data.main}/>
                <Resume data={this.state.data.resume}/>
                <Portfolio data={this.state.data.portfolio}/>
                <Testimonials data={this.state.data.testimonials}/>
                <Contact data={this.state.data.main}/>
                <Footer data={this.state.data.main}/>
            </div>
        );
    }
}

export default App;

import React, {Component} from 'react';

class Footer extends Component {
    render() {
        let networks, name, year;

        if (this.props.data) {
            networks = this.props.data.social.map(function (network) {
                return <li key={network.name}><a href={network.url}><i className={network.className}></i></a></li>
            });
            name = this.props.data.name;
            year = new Date().getFullYear();
        }

        return (
            <footer>

                <div className="row">
                    <div className="twelve columns">
                        <ul className="social-links">
                            {networks}
                        </ul>

                        <ul className="copyright">
                            <li>&copy; Copyright {year} <a title={name} href="http://www.patrickvogel.nl/">{name}</a></li>
                        </ul>

                    </div>
                    <div id="go-top">
                        <a className="smoothscroll" title="Back to Top" href="#home">
                            <i className="icon-up-open"></i>
                        </a>
                    </div>
                </div>
            </footer>
        );
    }
}

export default Footer;

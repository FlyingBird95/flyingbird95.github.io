import React, {Component} from 'react';

class Contact extends Component {
    render() {

        if (this.props.data) {
            var name = this.props.data.name
            var city = this.props.data.address.city;
            var country = this.props.data.address.country;
            var phone = this.props.data.phone;
            var email = this.props.data.email;
            var message = this.props.data.contactmessage;
        }

        return (
            <section id="contact">
                <div className="row section-head">
                    <div className="two columns header-col">
                        <h1><span>Get In Touch.</span></h1>
                    </div>
                    <div className="ten columns">
                        <p className="lead">{message}</p>
                        <br/>
                    </div>
                </div>
                <div className="row">
                    <div className="eight columns">
                        <form action="https://formspree.io/patrickvogel@live.nl" method="POST">
                            <fieldset>
                                <div>
                                    <label htmlFor="name">Name <span className="required">*</span></label>
                                    <input type="text" defaultValue="" size="35" id="name" name="name"
                                           onChange={this.handleChange}/>
                                </div>
                                <div>
                                    <label htmlFor="email">Email <span className="required">*</span></label>
                                    <input type="email" size="35" id="email" name="_replyto"
                                           onChange={this.handleChange}/>
                                </div>
                                <div>
                                    <label htmlFor="message">Message <span className="required">*</span></label>
                                    <textarea cols="50" rows="15" id="message" name="message"></textarea>
                                </div>
                                <div>
                                    <button className="submit" value="Send">Submit</button>
                                </div>
                            </fieldset>
                        </form>
                    </div>

                    <aside className="four columns footer-widgets">
                        <div className="widget widget_contact">
                            <h4>Address and Phone</h4>
                            <p className="address">
                                <span>{name}</span><br/>
                                <span>{city}</span><br/>
                                <span>{country}</span><br/>
                                <span>{phone}</span><br/>
                                <span><a href="mailto:patrickvogel@live.nl">{email}</a></span>
                            </p>
                        </div>
                    </aside>
                </div>
            </section>
        );
    }
}

export default Contact;

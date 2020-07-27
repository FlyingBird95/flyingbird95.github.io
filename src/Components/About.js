import React, {Component} from 'react';

class About extends Component {
    render() {
        let name, profilePic, resumeLink, city, country, email;

        if (this.props.data) {
            name = this.props.data.name;
            profilePic = "images/" + this.props.data.image;
            resumeLink = this.props.data.resumeLink;
            city = this.props.data.address.city;
            country = this.props.data.address.country;
            email = this.props.data.email;
        }

        return (
            <section id="about">
                <div className="row">
                    <div className="three columns">
                        <img className="profile-pic" src={profilePic} alt="Patrick Vogel Profile Pic"/>
                    </div>
                    <div className="nine columns main-col">
                        <div className="row">
                            <div className="columns contact-details">
                                <h2>Contact Details</h2>
                                <p className="address">
                                    <span>{name}</span><br/>
                                    <span>{city}</span><br/>
                                    <span>{country}</span><br/>
                                    <span><a href="mailto:patrickvogel@live.nl">{email}</a></span>
                                </p>
                            </div>
                            <div className="columns download">
                                <p>
                                    <a href={resumeLink} className="button" target="_blank">
                                        <i className="fa fa-download"></i>Download Resume
                                    </a>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        );
    }
}

export default About;

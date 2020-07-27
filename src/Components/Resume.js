import React, {Component} from 'react';

class Resume extends Component {
    render() {
        let skillMessage, education, work, skills;

        if (this.props.data) {
            skillMessage = this.props.data.skillMessage;
            education = this.props.data.education.map(function (education) {
                return (
                <div key={education.degree}>
                    <h3>{education.school}</h3>
                    <p className="info">
                        {education.degree} <span>&bull;</span><em className="date">{education.graduated}</em>
                    </p>
                    <p>{education.description}</p>
                </div>
                );
            });
            work = this.props.data.work.map(function (work) {
                return (
                    <div key={work.company}>
                        <h3>{work.company}</h3>
                        <p className="info">
                            {work.title}<span>&bull;</span> <em className="date">{work.years}</em>
                        </p>
                        <p className="newline">{work.description}</p>
                    </div>
                );
            });
            skills = this.props.data.skills.map(function (skills) {
                let projectImage = 'images/tech/' + skills.image;
                return (
                    <div key={skills.name} className="card three columns feature-item">
                        <div className="row" style={{"height": "150px"}}>
                            <img className='skill' alt={skills.name} src={projectImage}/>
                        </div>
                        <div className="row" style={{"height": "350px"}}>
                            <h5>{skills.name}</h5>
                            <p>{skills.description}</p>
                        </div>
                    </div>
                );
            });
        }

        return (
            <section id="resume">

                <div className="row work">
                    <div className="three columns header-col">
                        <h1><span>Work</span></h1>
                    </div>
                    <div className="nine columns main-col">
                        {work}
                    </div>
                </div>

                <div className="row education">
                    <div className="three columns header-col">
                        <h1><span>Education</span></h1>
                    </div>
                    <div className="nine columns main-col">
                        <div className="row item">
                            <div className="twelve columns">
                                {education}
                            </div>
                        </div>
                    </div>
                </div>

                <div className="row skill">
                    <div className="three columns header-col">
                        <h1><span>Favorite Tech</span></h1>
                    </div>
                    <div>
                        <div className="nine columns main-col">
                            <p className="lead center">{skillMessage}</p>
                        </div>
                        <div className="twelve columns main-col">
                            {skills}
                        </div>
                    </div>
                </div>
            </section>
        );
    }
}

export default Resume;

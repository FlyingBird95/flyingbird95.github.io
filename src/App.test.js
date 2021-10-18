import React from "react"
import ReactDOM from "react-dom"
import App from "./App"

it('renders without crashing', () => {
    const div = document.createElement('div');
    ReactDOM.render(<App/>, div);
});

// @ponicode
describe("getData", () => {
    let object
    let inst

    beforeEach(() => {
        object = [["George", "Pierre Edouard", "Pierre Edouard"], ["Jean-Philippe", "Jean-Philippe", "George"], ["George", "Edmond", "Anas"]]
        inst = new App.default(object)
    })

    test("0", () => {
        let callFunction = () => {
            inst.getData()
        }
    
        expect(callFunction).not.toThrow()
    })
})

// @ponicode
describe("componentDidMount", () => {
    let object
    let inst

    beforeEach(() => {
        object = [["Anas", "Pierre Edouard", "Anas"], ["George", "Michael", "Edmond"], ["Michael", "Anas", "Jean-Philippe"]]
        inst = new App.default(object)
    })

    test("0", () => {
        let callFunction = () => {
            inst.componentDidMount()
        }
    
        expect(callFunction).not.toThrow()
    })
})

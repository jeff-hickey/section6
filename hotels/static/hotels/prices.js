class App extends React.Component {

        constructor(props) {
            super(props);
            this.state = {data: null};
        }

    /** Invoked immediately after component is
     * added to the DOM.
     */
    componentDidMount() {
        this.load_prices()
    }

    load_prices() {
        const url = 'http://127.0.0.1:8000/prices';
        fetch(url)
            .then(response => response.json())
            .then(data => {
                this.setState({data: data});
            })
            .catch(error => console.error(url, error))
    }

    render() {
        return (
            <ul>
                {this.state.data && this.state.data.rooms.map((room) => {
                    // film is an object, just one or more properties to render
                    return <li key={room.id}>Room #{room.number}: {room.label}, price: ${room.price}</li>;
                })}
            </ul>
        );
    }
}

ReactDOM.render(< App/>, document.querySelector("#app"));


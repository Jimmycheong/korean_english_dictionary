var componentStyle = {
  height: "500px",
}

var cardPanelStyle = {
  minHeight: "350px"
}

var host_url = window.location.href

class Component extends React.Component {
  constructor(props){
    super(props)
    this.state = { 
        submittedWord : "",
        definition: ""
      }

    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event){
    event.preventDefault();
    var this_ = this
    if (event.target.value.length > 0 ){
      axios.get(host_url + "ranked_search/" + event.target.value)
      .then(function (response) {
        console.log("JUst returned!")
        $("#myInput").autocomplete({source: response.data});
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  }

  handleSubmit(event){
    event.preventDefault();
    var this_ = this
    var inputValue = $("#myInput").val().trim()
    if (inputValue.length > 0 ) {
      axios.get(host_url + "definition/" + inputValue)
      .then(function (response) {
        console.log("RESPONSE: ")
        console.log(response)
        this_.setState({
          submittedWord: inputValue,
          definition:response.data[inputValue]
        })
      })
      .catch(function (error) {
        console.log(error);
      });
    } else {
      this_.setState({
          submittedWord: "",
          definition: ""
        })
    }
  }

  render(){

    var definition = this.state.definition

    if (this.state.submittedWord == "") {
      if (this.state.definition == "" || this.state.definition == null) {
        definition =  "No definition found"
      }
      definition = ""
    }

    console.log("this.state.definition: ", this.state.definition)
    var searchedWord = (<h5>{definition}</h5>)

    return(
      <div>
        <div className="col s1"></div>
        <div className="col s5">
        <div className="card-panel" style={cardPanelStyle}>
          <h4 className="panel-header">Search for a term</h4>
          <br/><br/>
          <form className="input-field" onSubmit={this.handleSubmit}>
            <input className="searchInput" id="myInput" type="text" id="myInput" onChange={this.handleChange} ></input>
            <br/><br/>
            <input className="blue darken-3 waves-effect waves-light btn-large" type="submit" value="Submit"></input>
          </form>
          <br/><br/>
        </div>
        </div>
        <div className="col s5">
          <div className="card-panel" style={cardPanelStyle}>
            <div> 
              <h4 className="panel-header">Definition</h4>
              <br/><br/>         
              {searchedWord}
            </div>
          </div>
        </div>
        <div className="col s1"></div>
      </div>
      )
  }
}

ReactDOM.render(
  <div className="row">
    <Component name="Component 1"/>
  </div>,
  document.getElementById('component')
)

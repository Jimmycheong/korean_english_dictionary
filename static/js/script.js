
  var componentStyle = {
    height: "500px",
  }

  var host_url = window.location.href

    class Component extends React.Component {
      constructor(props){
        super(props)
        this.state = { 
            submittedWord : ""
          }

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
      }

      handleChange(event){
        event.preventDefault();
        var this_ = this
        if (event.target.value.length > 0 ){
          $.get(host_url + "search/" + event.target.value, function(data, status){
            $("#myInput").autocomplete({source: data});
          })
        }
      }

      handleSubmit(event){
        event.preventDefault();
        console.log("Submitted!")
        this.setState({submittedWord: $("#myInput").val()})
      }

      render(){
        var submittedWord = (this.state.submittedWord == '') ? <div></div> : (
          <div>          
            <h4>Submitted Word:</h4>
            <h3>{this.state.submittedWord}</h3>
          </div>
          )

        return(
          <div>
            <div className="col s3"></div>
            <div className="col s6">
            <div className="card-panel">
              <h4>Search for a term</h4>
              <br/><br/>
              <form onSubmit={this.handleSubmit}>
                <input class="searchInput" id="myInput" type="text" id="myInput" onChange={this.handleChange} ></input>
                <br/><br/>
                <input className="blue darken-3 waves-effect waves-light btn-large" type="submit" value="Submit"></input>
              </form>
              <br/><br/>
              {submittedWord}
            </div>
            </div>
            <div className="col s3"></div>
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

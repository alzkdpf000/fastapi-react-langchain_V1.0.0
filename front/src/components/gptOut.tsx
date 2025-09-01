const Output = ({result} :{result:string} )=>{
    return (<div style={{ alignSelf: "flex-start", background: "#fff", color: "#222", padding: "10px 16px", borderRadius: 16, maxWidth: "80%", border: "1px solid #e0e0e0" }}>
        {result}
      </div>)
}

export default Output;

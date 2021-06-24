console.log("working")
const tableBody = document.getElementById('table-body')

fetch("https://api.covid19india.org/data.json")
.then(res => res.json())
.then(data => {
    
    data.statewise.map(stateData => (
        tableBody.innerHTML += ` <tr>
                                    <td>${stateData.state}</td>
                                    <td>${stateData.active}</td>
                                    <td>${stateData.recovered}</td>
                                    <td>${stateData.deaths}</td>
                                 
                                </tr>`
        
    ))
 
})
.catch(err => console.log(err))
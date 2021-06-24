// console.log("Working")

let  btn = document.getElementById("btn")
let cardContaner = document.getElementById("cardContainer")

btn.addEventListener('click', (e) => {
    e.preventDefault()

    let pincode = document.getElementById('pincode').value
    let date = document.getElementById('date').value




    let url = `https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=${pincode}&date=${date}`
    // let url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=277001&date=29-05-2021"

    fetch(url)
    .then(res => res.json())
    .then(data => {
        let centers = data.centers
        centers.map( center => (
            cardContaner.innerHTML += `
                                        <div class="col">
                                        <div class="card">
                                            <div class="card-body">
                                                <h5 class="card-title">${center.name}</h5>
                                                <p class="card-text">${center.address}</p>
                                                <small>From :- ${center.from} To :- ${center.to}</small>
                                                <p>${center.sessions[0].vaccine}</p>
                                                <div class="row">
                                                    <div class="col-sm-6">
                                                        <p>Age Limit : ${center.sessions[0].min_age_limit}</p>
                                                    </div>
                                                    <div class="col-sm-6">
                                                        <p>Availability :${center.sessions[0].available_capacity} </p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                `
        ))
        
    })
    .catch(err => console.log(err))

})

// let url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=277001&date=29-05-2021"

// fetch(url)
// .then(res => res.json())
// .then(data => console.log(data.centers))
const customerContainer = document.querySelector("#customer-container");

// Render the received data.
const renderCustomer = ({ data }) => {
  const { customerSearch: customer } = data;

  if (customer !== null)
    customerContainer.insertAdjacentHTML('afterbegin',
        '<ul> ' +
          '<li>First name: '+customer.firstName+'</li> ' +
          '<li>Last name: '+customer.lastName+'</li> ' +
          '<li>Email: '+customer.email+'</li> ' +
          '<li>Gender: '+customer.gender+'</li> ' +
          '<li>Company: '+customer.company+'</li> ' +
          '<li>Title: '+customer.title+'</li> ' +
          '<li>city: '+customer.city+'</li> ' +
          '<li>Coordinates: (lat:'+customer.lat+', lng:'+customer.lng+')</li> ' +
        '</ul>'
    );
  else
    customerContainer.insertAdjacentHTML('afterbegin', '<h2>Customer not found.</h2>');

}


// Fetch Customer data
const loadCustomer = (id) => {

  // Fetch customer's details query.
  const query = `{ 
    customerSearch(id:${id}){
      id,
      firstName,
      lastName,
      email,
      gender,
      company,
      title,
      city,
      lat,
      lng
    }
  }`

  // Query the API and render it after receiving the data.
  fetch('http://127.0.0.1:8000/graphql/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
       body: JSON.stringify({ query })
  })
      .then(res => res.json())
      .then(data=> renderCustomer(data));
}



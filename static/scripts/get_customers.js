const customerContainer = document.querySelector("#customer-container");

// Render the received data.
const renderCustomers = ({ data }) => {
  // Place the json data in an array.
  const { customers: allCustomers = [] } = data;

  // Create a fragment to put all the users in.
  const customerFragment = document.createDocumentFragment();
  const customerList = document.createElement('ul');

  // Loop through the customers' list and render them.
  if (allCustomers.length>0)
    allCustomers.forEach((customer) => {
      const customerListItem = document.createElement('li');
      const customerListLink = document.createElement('a');

      customerListLink.href = "http://127.0.0.1:8000/customer/"+customer.id+"/";
      customerListLink.textContent = "Click To View";

      customerListItem.textContent = `${customer.id}: ${customer.firstName} ${customer.lastName} - `;
      customerListItem.appendChild(customerListLink);
      customerList.appendChild(customerListItem);
    });

  else {
    customerContainer.insertAdjacentHTML('afterbegin', '<h2>No customers found.</h2>');
  }

  // Append the newly created HTML to the previously created fragment.
  customerFragment.appendChild(customerList);
  customerContainer.appendChild(customerFragment);
}

// Query the API using the specified query string.
const loadCustomers = () => {
  fetch('http://127.0.0.1:8000/graphql/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ query })
  })
      .then(res => res.json())
      .then(renderCustomers);
}

// Fetch all customers query.
const query = `{ customers { id, firstName, lastName } }`

// Start loading data after the DOM finishes loading its content.
document.addEventListener('DOMContentLoaded', function () {
  loadCustomers()
});
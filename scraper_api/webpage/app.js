"use strict";
const getSearch = async () => {
  var title = document.getElementById("title").value;
  var keywords = document.getElementById("keywords").value;
  const mydata = { title: title, keywords: keywords };
  const response = await fetch("http://127.0.0.1:2000/result", {
    method: "POST",
    body: JSON.stringify(mydata), // string or object
    headers: {
      "Content-Type": "application/json",
    },
  });
  var data = await response.json(); //extract JSON from the http response

  var myArr = [];
  for (var [key, value] of Object.entries(data)) {
    myArr.push(value);
  }

  $("th").on("click", function () {
    var column = $(this).data("column"); // data attribute used to identify the column clicked
    var order = $(this).data("order");
    var text = $(this).html();
    text = text.substring(0, text.length - 1);

    if (order == "desc") {
      $(this).data("order", "asc");
      myArr = myArr.sort((a, b) => (a[column] > b[column] ? 1 : -1));
      text += "&#9660";
    } else {
      $(this).data("order", "desc");
      myArr = myArr.sort((a, b) => (a[column] < b[column] ? 1 : -1));
      text += "&#9650";
    }
    $(this).html(text);
    buildTable(myArr);
  });

  buildTable(myArr);
  function buildTable(data) {
    var table = document.getElementById("tableContent");
    table.innerHTML = ""; //clears out the contents when build table is called
    for (var i = 0; i < data.length; i++) {
      var row = `
      <tr>
          <td><a href='${data[i].link}'>${data[i].title}</a></td>
          <td>${data[i].description}</td>
          <td>${data[i].ranking}</td>
          <td>${data[i].citations}</td>
      </tr>
      `;
      table.innerHTML += row;
    }
  }
};

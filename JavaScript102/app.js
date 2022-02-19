// let list = document.querySelector('ul');
// let input = document.querySelector('input#item');
// let ShoppingList = [];

// function AddItemClick(){
//     ShoppingList.push(input.value)
// }


new Promise( (res, rej) => {
    setTimeout(() => res(1), 6000);
  }).then( (res) => {
    console.log(res); // 1
    return res*2
  }).then( (res) => {
    console.log(res); // 2
  });
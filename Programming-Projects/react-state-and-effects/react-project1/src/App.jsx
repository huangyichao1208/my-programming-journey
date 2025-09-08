import { useState } from "react";

function Cart() {
  const [cart, setCart] = useState([]);

  const addItem = (item) => {
    setCart([...cart, item]);
  };

  return (
    <>
      <button onClick={() => addItem("苹果")}>加入苹果</button>
      <button onClick={() => addItem("香蕉")}>加入香蕉</button>
      <ul>
        {cart.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </>
  );
}
export default Cart;
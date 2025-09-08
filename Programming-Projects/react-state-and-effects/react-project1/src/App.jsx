import { useState } from "react";
import "./App.css"; // 引入 CSS 文件

function ModalExample() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <button onClick={() => setIsOpen(!isOpen)}>切换弹窗</button>
      {isOpen && <div>这是一个弹窗</div>}
    </>
  );
}

export default ModalExample;
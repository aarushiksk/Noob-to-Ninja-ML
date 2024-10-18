const predict = (e) => {
  e.preventDefault();
  const output = document.getElementById("output");

  const input_a = document.getElementById("a");
  const input_b = document.getElementById("b");
  const input_c = document.getElementById("c");

  const a = parseFloat(input_a.value);
  const b = parseFloat(input_b.value);
  const c = parseFloat(input_c.value);
  if (
    a > 10 ||
    a < 0 ||
    b < 0 ||
    b > 10 ||
    c > 10 ||
    c < 0 ||
    isNaN(a) ||
    isNaN(b) ||
    isNaN(c)
  ) {
    output.textContent =
      "Invalid Input : Please enter value between 0.00 to 10.00";
    output.style.color = "red";
    return;
  }
  console.log(a, b, c);
  const spi = query(a, b, c);

  output.textContent = "Predicited Approximate CGPA : " + spi.toFixed(2);
  output.style.color = "green";
};
const query = (a, b, c) => {
  const mean_bias = 1.99862;
  const coef = [0.9131820967793465, 0.9317458146810532, 0.969840207695961];
  const spi = (a * coef[0] + b * coef[1] + c * coef[2] + mean_bias) / 3;
  return spi;
};

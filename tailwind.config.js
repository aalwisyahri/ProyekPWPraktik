/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html"
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Poppins", "sans-serif"], // Tambahkan font utama
    },
  },
  plugins: [],
}
}

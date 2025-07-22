// Sign Up Form
const signupForm = document.getElementById('signupForm');
if (signupForm) {
  signupForm.addEventListener('submit', function (e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;
    const confirm = document.getElementById('confirmPassword').value;

    if (password !== confirm) {
      alert('Passwords do not match!');
      return;
    }

    // Save user to localStorage (simulated "backend")
    localStorage.setItem('mindmate_user', JSON.stringify({ name, email, password }));
    alert('Account created! You can now sign in.');
    window.location.href = 'signin.html';
  });
}

// Login Form
const loginForm = document.getElementById('loginForm');
if (loginForm) {
  loginForm.addEventListener('submit', function (e) {
    e.preventDefault();
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    const user = JSON.parse(localStorage.getItem('mindmate_user'));

    if (user && user.email === email && user.password === password) {
      alert(`Welcome back, ${user.name}!`);
      // Proceed to dashboard or app page
    } else {
      alert('Invalid credentials!');
    }
  });
}

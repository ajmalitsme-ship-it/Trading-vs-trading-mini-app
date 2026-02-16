const tg = window.Telegram.WebApp;
tg.expand();

const userId = tg.initDataUnsafe.user.id;

async function loadUser() {
  const res = await fetch("/get_user", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ user_id: userId })
  });

  const data = await res.json();
  document.getElementById("coins").innerText = "Coins: " + data.coins;
}

async function watchAd() {
  alert("Simulated Ad Watching...");

  const res = await fetch("/watch_ad", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ user_id: userId })
  });

  const data = await res.json();
  document.getElementById("coins").innerText = "Coins: " + data.coins;
}

async function withdraw() {
  const res = await fetch("/withdraw", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ user_id: userId })
  });

  const data = await res.json();
  alert(data.status || data.error);
}

loadUser();

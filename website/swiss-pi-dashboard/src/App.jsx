import Login from "./pages/Login.jsx";
import {Route, Routes} from "react-router-dom";
import Registrieren from "./pages/Registrieren.jsx";
import Hauptseite from "./pages/Hauptseite.jsx";
import Nmap from "./pages/Nmap.jsx";
import Suricata from "./pages/Suricata.jsx";
import Cowrie from "./pages/Cowrie.jsx";
import Mitre from "./pages/Mitre.jsx";

function App() {
  return (
      <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/registrieren" element={<Registrieren />} />
          <Route path="/" element={<Hauptseite />} />
          <Route path="/nmap" element={<Nmap />} />
          <Route path="/suricata" element={<Suricata />} />
          <Route path="/cowrie" element={<Cowrie />} />
          <Route path="/mitre" element={<Mitre />} />
      </Routes>
  )
}

export default App

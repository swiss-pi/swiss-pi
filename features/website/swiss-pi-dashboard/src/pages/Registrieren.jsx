import Menue from '../components/Menue.jsx'
import './Login.css'

function Registrieren() {
    return (
        <div>
            <Menue position="rechts" mitLogout={true} />

            <h1>Swiss-Pi</h1>

            <div className="login-box">
                <label>Benutzername:</label>
                <input type="text" />

                <label>Passwort:</label>
                <input type="password" />

                <label>Passwort wiederholen:</label>
                <input type="password" />
            </div>

            <button className="signup-button">Sign up</button>
        </div>
    )
}

export default Registrieren

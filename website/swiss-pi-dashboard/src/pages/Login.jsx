import { Link } from 'react-router-dom'
import Menue from '../components/Menue.jsx'
import './Login.css'

function Login() {
    return (
        <div>
            <Menue position="rechts" mitLogout={true} />
            <h1>Swiss-Pi</h1>

            <div className="login-box">
                <h2>Login</h2>

                <label>Benutzername:</label>
                <input type="text" />

                <label>Passwort:</label>
                <input type="password" />

                <div className="login-links">
                    <Link to="/registrieren">Registrieren</Link>
                    <Link to="/passwort-vergessen">Passwort vergessen?</Link>
                </div>
            </div>
        </div>
    )
}

export default Login

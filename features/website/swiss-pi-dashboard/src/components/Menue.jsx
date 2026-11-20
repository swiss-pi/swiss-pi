import { useState } from 'react'
import { Link } from 'react-router-dom'
import './Menue.css'

function Menue({ position = 'links', mitLogout = false }) {
    const [offen, setOffen] = useState(false)

    return (
        <div className={'menue menue-' + position}>
            <button className="menue-button" onClick={() => setOffen(!offen)}>☰</button>

            {offen && (
                <ul className="menue-liste">
                    <li><Link to="/settings">Settings</Link></li>
                    <li><Link to="/about">About</Link></li>
                    <li><Link to="/datenschutz">Privacy Policy</Link></li>
                    {mitLogout && <li><Link to="/login">Log out</Link></li>}
                </ul>
            )}
        </div>
    )
}

export default Menue

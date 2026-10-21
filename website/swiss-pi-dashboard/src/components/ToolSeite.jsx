import { Link } from 'react-router-dom'
import Menue from './Menue.jsx'
import Kachel from './Kachel.jsx'
import './ToolSeite.css'

function ToolSeite({ titel, kacheln, children }) {
    return (
        <div className="tool-seite">
            <Menue position="rechts" mitLogout={true} />

            <div className="tool-kopf">
                <Link to="/" className="zurueck-link">← Zurück zur Hauptwebsite</Link>
                <h1>{titel}</h1>
            </div>

            <div className="tool-kacheln">
                {kacheln.map((k) => (
                    <Kachel key={k.name} name={k.name} anzahl={k.wert} />
                ))}
            </div>
            
            {children}
        </div>
    )
}

export default ToolSeite

import ToolSeite from '../components/ToolSeite.jsx'

function Nmap() {
    return (
        <ToolSeite
            titel="Swiss-Pi-Nmap"
            kacheln={[
                { name: 'Geräte im Netz', wert: '–' },
                { name: 'IP', wert: '0.0.0.0' },
                { name: 'Riskante Ports', wert: '–' },
                { name: 'Letzter Scan', wert: '–' },
            ]}
        />
    )
}

export default Nmap

function Kachel({ name, anzahl, farbe }) {
    return (
        <div className="kachel" style={{ borderColor: farbe }}>
            <div className="kachel-name">{name}</div>
            <div className="kachel-anzahl">{anzahl}</div>
        </div>
    )
}

export default Kachel

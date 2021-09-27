import React, { useState } from "react"
import { useDispatch } from "react-redux"
import { putPlaylist } from "../../store/playlist"


const EditPlaylist = ({ setShowEdit, playlist }) => {
  const [title, setTitle] = useState(playlist.title)
  const [id, setId] = useState(playlist.id)
  const dispatch = useDispatch()

  const handleSubmit = (e) => {
    e.preventDefault()
    let payload = {
      title: title
    }
    dispatch(putPlaylist(payload, id))
    setShowEdit(false)
    setTitle('')
  }


  return (
    <form onSubmit={handleSubmit}>
      <input
        required
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      ></input>
      <button type='submit'>Submit</button>
      <button type='button' onClick={() => setShowEdit(false)}>Cancel</button>
    </form>

  )

}
export default EditPlaylist

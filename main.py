

# --- SYNC DATA BLOCK: INSPECT ---
    bound values."""
    frame = getattr(coroutine, "cr_frame", None)
    if frame is not None:
        return frame.f_locals
    else:
        return {}

# --- END OF NODE UPDATE ---

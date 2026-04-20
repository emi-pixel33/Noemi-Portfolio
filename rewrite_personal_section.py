from pathlib import Path

path = Path('index.html')
with path.open('r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<!-- ============ PERSONAL SECTION ============ -->'
end_marker = '<div class="section-title">\n                <h2>My Resume</h2>'

start = text.find(start_marker)
if start == -1:
    raise SystemError('start marker not found')
end = text.find(end_marker, start)
if end == -1:
    raise SystemError('end marker not found')

replacement = '''    <!-- ============ PERSONAL SECTION ============ -->
    <section id="personal">
        <div class="container">
            <div class="personal-header">
                <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&q=80" alt="Noemi Portrait" class="profile-pic">
                <h1>Noemi Estigoy</h1>
                <p class="personal-tagline">Web Developer | UX Enthusiast | Storyteller</p>
                <p class="personal-location">?? Manila, Philippines</p>
            </div>

            <div class="photo-gallery">
                <h3>Friends & Network</h3>
                <div class="gallery-photos">
                    <div class="photo-item">
                        <img src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=400&q=80" alt="Senior High School Friends">
                        <div class="photo-overlay">Senior High School Friends</div>
                    </div>
                    <div class="photo-item">
                        <img src="https://images.unsplash.com/photo-1517841905240-472988babdf9?w=400&q=80" alt="College Friends">
                        <div class="photo-overlay">College Friends</div>
                    </div>
                    <div class="photo-item">
                        <img src="https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=400&q=80" alt="Project Team">
                        <div class="photo-overlay">Project Team</div>
                    </div>
                </div>
            </div>

            <div class="section-title">
                <h2>My Resume</h2>
            </div>
'''

new_text = text[:start] + replacement + text[end:]
with path.open('w', encoding='utf-8') as f:
    f.write(new_text)
print('Replaced personal section block successfully.')
